# 棚（カテゴリ2階層の索引）

34項目を、大分類 → 小分類の2階層で並べたもの。対訳（世界標準の名前）は [`translation-map.md`](translation-map.md)、
各制度の本文は [`institutions/`](institutions/) にある。

## 設計と意思決定

### 上流の設計

- skill `map-first` — 全体図を先に描く（ADR）
- doc `decision-package` — 人に判断を求めるときの入力規格5点
- doc `three-layers-and-four-graphs` — 運転の3層と4つのグラフ

### 案を磨く

- skill `sentakuatsu` — 採点器を前提に案を世代ループで進化させる
- skill `verify-before-build` — 一次資料に接地してから作る

## レビューと検収

### 敵対監査

- skill `kansa` — 監査と検収の共通入口
- doc `adversarial-audit` — 完了の定義・検収・新鮮な目・裁定の4層
- doc `two-stage-check` — 安い別モデルの独立検査
- doc `crosswatch` — 並走セッションの相互監査

### 合否の規律

- doc `definition-of-done` — 完了は検証コマンドと実出力で証明する
- doc `no-self-acceptance` — 自分の成果物に自分で合格を出さない
- doc `audit-completion-gate` — 未監査を合格と呼ばせない

## 人間ゲートと監督

### 止める場所を決める

- doc `stop-and-nonstop-questions` — 可逆性で問いを2種類に機械分類する
- doc `question-queue` — 人への問いを1本のキューに集約する
- doc `question-catalog` — 出典義務つきの問いカタログ
- skill `toi` — 問いを通す

### 監督が効いているか測る

- doc `oversight-metrics` — 監督の質を週次で実測する
- doc `risk-tiered-effort` — リスク階層に応じて推論予算を配分する

## 結線（制度を動かす）

### 結線の原則と台帳

- doc `wiring-or-it-doesnt-exist` — 結線されていない制度は存在しない
- doc `wiring-ledger` — 何が何を発火させるかの台帳
- doc `wiring-check` — 制度文書と現物の自動突合

### 結線の落とし穴

- doc `injection-is-not-compliance` — 注入と発火証明と遵守観測は別物
- doc `kill-switch-and-restore` — 一斉停止と一斉再開を対にする

## 実装の回し方

### 委譲

- skill `toryo` — 設計と施工を分ける

### 横展開

- skill `franchise-kaizen` — 旗艦からマニュアル化して全体へ
- skill `mondai-kaizen` — ベンチマーク駆動でコンテンツの質を上げる

## 体験と画面

### 作るとき

- skill `ui-kihon` — 操作要素の単位で設計し実機で検品する

### 歩いて壊すとき

- skill `persona-walk` — 離脱しうる人の目で実画面を歩く

## 知識の蓄積

### 型の台帳

- doc `pattern-catalog` — 症状から確立された解法を引く
- doc `mental-models-canon` — 人類の思考の型のカノン

### 案件の資産化

- skill `l2package` — 案件クローズごとに1枚に畳む
- skill `seiri` — 出し切って核を1つ特定する
- skill `shinjigyo` — アイデアから収益までの一本道

## 公開と機微

### 出口検査

- doc `publication-registry` — 置き場所ではなくファイル単位で公開物を判定する

## 件数

- 索引に並んでいる項目: **34**（skill 13 ＋ 制度文書 21）

