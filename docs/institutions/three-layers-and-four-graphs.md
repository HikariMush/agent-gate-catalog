# 運転の3層と4つのグラフ

**1行**: 運転の既定は境界条件つきの自律。境界は外向き・不可逆・お金だけで、境界内は自律、判定不能は止める側に倒す。**行為単位の承認を増やす方向の設計をしない**。新しい制度を作るときは「結線 / 正本 / 実出力 / 監査」の4点の所在を宣言してから作る。

## 世界標準の名前

human-in / on-the-loop / human-in-command の3類型 ＋ control graph / knowledge graph / execution trace / improvement graph。根拠は automation bias・approval fatigue・Ironies of Automation（Bainbridge 1983）。

## 発火（何がこれを動かすか）

セッション開始時の手順（弱い結線）＋ 新設時の宣言。

## 実測 / 観測

承認回数が増えるほど人の注意は下がる、が設計の前提。**承認を増やす方向の改善案は採らない**。

## 注記

**正当な human-out-of-the-loop は存在しない**。out は設計するものではなく、on の設計から漏れた場所に発生する。どの監視面にも載らない自律実行を見つけたら、欠落として台帳に載せる。

---

対訳表: [`../translation-map.md`](../translation-map.md)
