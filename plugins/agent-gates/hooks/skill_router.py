#!/usr/bin/env python3
"""UserPromptSubmit フック — プロンプトの語彙から、当てるべき skill を名指しでリマインドする。

## 何を発火させる結線か

このリポジトリの skill は「その場面では必ず使う」と定義されているが、**発火がモデルの気づきに
依存している**限り、入口の文言が想定と違う形（評価依頼・雑談・単なる質問）で来たときに素通りする。
実際に、事業の相談が「これは現実的？」という評価依頼の形で来たために該当 skill が起動せず、
3ターン止まった事例がある。この hook は、その素通りを語彙で機械的に拾う結線であり、
制度の側から見れば「skill を思い出させる発火経路」にあたる。

判断はモデルに残す。この hook は強制ではなく**リマインドだけ**を行う。

## 設計方針

1. **誤検知を安くする** — 注入文は短く、末尾に必ず「関係なければ無視してよい」を付ける
2. **fail-open** — 例外が出たら黙って `{}` を返す。会話を壊すより見逃すほうがよい
   （hook が壊れてもプロンプトは止まらない）
3. **ルールは表で持つ** — skill を足すときは RULES に1行足すだけで済む形にする
4. **外部依存を持たない** — 標準ライブラリのみ。設定ファイルもネットワークも使わない

## 使い方

`hooks.json` から `UserPromptSubmit` で呼ばれる。標準入力の JSON からプロンプト本文を読み、
一致した skill があれば `hookSpecificOutput.additionalContext` に短い注入文を返す。
一致しなければ `{}` を返す（何も起きない）。
"""

import json
import re
import sys

# (skill 名, 強い語彙, 弱い語彙, 1行の説明)
#   強い語彙が1つでも当たれば注入する。弱い語彙は2つ以上当たったときだけ注入する。
RULES = [
    ("map-first", ["全体図", "設計して", "設計案", "方針を決め", "新しい仕組み", "他の案", "構造化して", "なぜこの案"],
     ["設計", "方針", "作り方", "進め方", "新機能"],
     "解決策へ直行する前に全体図（構造化→既知手法の照合→αβγ+推奨→図1枚→記録）を描く"),
    ("kansa", ["監査して", "検収して", "完了報告", "レビューして", "本当に終わ", "証拠を出"],
     ["監査", "検収", "確認して", "妥当か"],
     "完了は検証コマンドと実出力で判定し、自己検収を禁じる。公開・課金・go 判定の前は必ず通す"),
    ("ui-kihon", ["使いづら", "UX", "ボタン", "導線", "画面を作", "レイアウト", "デザイン整え"],
     ["画面", "UI", "配置", "操作性", "フォーム"],
     "画面の宣言→全操作要素を表にする→配置と美しさを別の目で攻撃→実機で検品"),
    ("seiri", ["ぐちゃぐちゃ", "思考の整理", "整理したい", "ダンプ", "壁打ち", "抱えすぎ", "何から手をつけ"],
     ["整理して", "まとめたい", "棚卸し", "洗い出"],
     "出し切る→多軸で分類→核を1つ→5つの行き先に仕分け→1件ずつ着工。ダンプ中は相槌のみ"),
    ("toryo", ["実装して", "作って", "直して", "バグ", "修正して"],
     ["実装", "コード", "機能追加"],
     "設計と施工を分ける。実装は背後のサブエージェントへ委譲し、検収より先に次を積む"),
    ("verify-before-build", ["一次資料", "仕様に従", "法令", "試験形式", "API 仕様", "絶対に外せない"],
     ["仕様", "規格", "正確に"],
     "外部の権威に依存する実装は、一次資料の取得→設計案→敵対監査→改訂→既存資産確認→実装の順"),
    ("persona-walk", ["ユーザー目線", "憑依", "ペルソナ", "歩いて", "離脱"],
     ["体験", "使ってみて", "第一印象"],
     "実画面を離脱しうる人の目で歩き、各画面で「離脱するならここ」を必ず1つ言う"),
    ("shinjigyo", ["新しい事業", "新規事業", "次の商売", "で稼げ", "事業を立ち上げ", "アイデア出し"],
     ["事業", "収益", "商品化", "価格"],
     "アイデア→顧客→商品と価格→go/kill→最小の売り物→試算→集客→営業→納品→月次判断の一本道"),
    ("toi", ["問通せ", "問い通せ", "深さ監査", "詰まって", "何をすべきか分から"],
     ["行き詰", "停滞", "見直し"],
     "答えではなく問いの正本を通す。回答は一次資料に接地させ、機械ゲートを通るまで未回答"),
    ("sentakuatsu", ["選択圧", "進化させ", "案を磨", "世代"],
     ["複数案", "比較して", "どれがいい"],
     "採点器を先に用意し、独立生成→立場固定の変異→選択の世代ループで設計案を進化させる"),
    ("l2package", ["案件クローズ", "納品した", "型にして", "パッケージ化して残"],
     ["振り返り", "次に活か"],
     "案件クローズごとに解・解き方・再利用条件を13行に畳み、2軸タグで索引する"),
    ("franchise-kaizen", ["横展開", "全店", "旗艦", "他のアプリにも"],
     ["展開", "複数サイト", "同じ構成"],
     "旗艦1つに監査を集中→発見/解決/検収手法をマニュアル化→全体へ展開→還流"),
    ("mondai-kaizen", ["コンテンツの質", "解説を良く", "設問", "競合を分析"],
     ["中身の質", "教材", "本文の改善"],
     "ベンチマークでギャップを測り、AI ゼロで作れる部分を先に実測してから生成に頼る"),
]

TAIL = "（関係なければ無視してよい）"


def read_prompt() -> str:
    """標準入力の JSON からプロンプト本文を取り出す。キー名は環境差を吸収する。"""
    try:
        raw = sys.stdin.read()
    except Exception:
        return ""
    if not raw.strip():
        return ""
    try:
        data = json.loads(raw)
    except Exception:
        return raw
    if not isinstance(data, dict):
        return ""
    for key in ("prompt", "user_prompt", "userPrompt", "message", "text", "content"):
        v = data.get(key)
        if isinstance(v, str) and v.strip():
            return v
    return ""


def match(prompt: str):
    """当たった skill を (名前, 説明) で返す。強い語彙は1つ、弱い語彙は2つ以上で当たり。"""
    p = prompt.lower()
    hits = []
    for name, strong, weak, note in RULES:
        if any(w.lower() in p for w in strong):
            hits.append((name, note, 2))
            continue
        if sum(1 for w in weak if w.lower() in p) >= 2:
            hits.append((name, note, 1))
    hits.sort(key=lambda h: -h[2])
    return hits[:2]


def build_context(prompt: str) -> str:
    hits = match(prompt)
    if not hits:
        return ""
    lines = ["この話題に対応する skill がこの環境に入っている:"]
    for name, note, _ in hits:
        lines.append(f"- `/{name}` — {note}")
    lines.append(TAIL)
    return "\n".join(lines)


def main() -> None:
    text = build_context(read_prompt())
    if not text:
        print("{}")
        return
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": text,
        }
    }, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # fail-open: hook が壊れてもプロンプトを止めない
        print("{}")
