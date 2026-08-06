# 並走セッションの相互監査

**1行**: 同時に動いている複数のエージェント・セッションが、追記のみの台帳1本を介して ①互いの作業を拾い ②互いの成果物を敵対監査し ③互いの停止を検知し ④**人に投げる必要のなかった問いを投げているセッションに突っ込む**。自分の項目を自分で閉じることを禁止する。

## 世界標準の名前

**(b) 新レール候補**。最近縁 = Trust Without Trusting（arXiv:2605.06738。"co-equal, mutually distrusting peers under a shared charter"）／ blackboard architecture・ledger-state stigmergy（台帳経由の間接協調）／ multi-agent debate ／ over-escalation（"the escalation trap"）。

## 発火（何がこれを動かすか）

10分ごとの定期実行が4条件を判定し、結果を各セッションへ注入する。

## 実測 / 観測

別セッションが合格を出した成果物の率 12.0%（7/59件・2026-08-07T05:50:02 生成の版）。台帳に記録した稼働セッションの率 50%（2/4）。**制度はまだ名目上しか動いていない**。

## 注記

**この設計は2026年の実務側の推奨と逆を向いている**（「peer どうしを協働させるなら arbiter を残せ」「open mesh の peer-to-peer は本番で問題が多い」）。採用する場合はこの点を承知した上で判断すること。Trust Without Trusting との差分は、①検証の対象が規則適用ではなく**成果物の質**であること ②**人の席があるので過剰エスカレーションの条件が存在する**こと の2点。

---

対訳表: [`../translation-map.md`](../translation-map.md)
