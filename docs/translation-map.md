# 対訳表（公開版・34項目）

このリポジトリで配る型を、世界に既にある名前へ対応づけた表。**既知の概念のカタログ実装として出す**方針で、
英語名を併記する。属地・案件固有のものは公開版から落としてあるので、内部の全項目数とは一致しない。

凡例: **(a)** = 世界に確立名がある / **(b)** = 検索で同じ運用単位が見つからず、独立した検収者の承認を経て新レール候補として出すもの

## skill として配布するもの（13本）

| skill | 中身（1行） | 世界標準の名前 |
|---|---|---|
| `kansa` | 敵対監査と検収の共通入口 | Adversarial review / red team review + fresh-eyes review |
| `map-first` | 解決策への直行を禁止し全体図を先に描く | Architecture Decision Record (Nygard 2011) / design doc / RFC |
| `ui-kihon` | 画面と操作要素の単位で設計し実画面で検品する | Nielsen's 10 usability heuristics + Laws of UX + heuristic evaluation |
| `seiri` | 出し切り→多軸分類→核の特定→1件ずつ着工 | GTD + faceted classification (Ranganathan) + prototype theory (Rosch) |
| `sentakuatsu` | 採点器を前提に設計案を世代ループで進化させる | Evolutionary search with LLMs (reflective prompt evolution) + LLM-as-a-judge |
| `l2package` | 案件クローズごとに解と解き方と再利用条件を1枚に畳む | Lessons learned register / project closeout + blameless postmortem |
| `toryo` | 設計と施工を分け、実装を背後のサブエージェントに委譲する | Orchestrator-worker pattern + Theory of Constraints |
| `verify-before-build` | 外部の権威に依存する実装で一次資料に接地してから作る | Spec-driven development / context grounding + design review with red team |
| `persona-walk` | 実画面を離脱しうる人の目で歩き衝突点を抽出する | Cognitive walkthrough (Lewis, Polson, Wharton, Rieman 1990 CHI) + persona |
| `franchise-kaizen` | 旗艦1つに監査を集中しマニュアル化して全店へ展開する | Yokoten (Toyota) + pilot/lighthouse site rollout + playbook |
| `mondai-kaizen` | ベンチマークからギャップを測りコンテンツの質を上げる | Competitive benchmarking + quality gate + deterministic-first / model cascade |
| `shinjigyo` | アイデアから収益までを段と gate で一本道にする | Stage-Gate (Cooper) + customer discovery / lean startup |
| `toi` | 出典義務つきの問いカタログと回答の機械ゲート | **(b) 新レール候補。最近縁 = structured analytic techniques / policy-enforced generation** |

## 制度文書として載せるもの（21件）

| 文書 | 中身（1行） | 世界標準の名前 |
|---|---|---|
| [`wiring-or-it-doesnt-exist`](institutions/wiring-or-it-doesnt-exist.md) | 結線されていない制度は存在しない | Policy as code / compliance as code / その裏返しの失敗名 paper compliance, shelfware |
| [`wiring-ledger`](institutions/wiring-ledger.md) | どの制度が何によって発火するかの台帳 | Control inventory / control registry / CMDB |
| [`wiring-check`](institutions/wiring-check.md) | 制度文書の散文の主張と現物の自動突合 | **(b) 新レール候補。最近縁 = configuration drift detection / doctest / ARPaCCino / PROPARAG** |
| [`stop-and-nonstop-questions`](institutions/stop-and-nonstop-questions.md) | 人への問いを可逆性で2種類に機械分類する | HITL approval gate + lazy consensus (ASF) + irreversibility-based gating + pocket veto |
| [`question-queue`](institutions/question-queue.md) | 人の判断が要る問いを1本のキューに集約する | Escalation policy / decision queue + policy registry + approval fatigue 対策 |
| [`decision-package`](institutions/decision-package.md) | 人に判断を求めるときの入力規格5点 | Decision brief / decision memo + pre-mortem (Klein) + assumption log (PMBOK) |
| [`adversarial-audit`](institutions/adversarial-audit.md) | 完了の定義・検収・新鮮な目・裁定の4層 | Red teaming / adversarial review + Structured Analytic Techniques (Heuer) |
| [`definition-of-done`](institutions/definition-of-done.md) | 完了は検証コマンドとその実出力で証明する | Definition of Done + audit evidence + deadman's switch |
| [`no-self-acceptance`](institutions/no-self-acceptance.md) | 実装した本人が自分の成果物に合格を出せない | Four-eyes principle / maker-checker / Segregation of Duties |
| [`audit-completion-gate`](institutions/audit-completion-gate.md) | 未監査を合格と呼ばせない・監査の滞留を検知する | QAIP (IIA) / external quality assessment + sufficient appropriate audit evidence |
| [`crosswatch`](institutions/crosswatch.md) | 並走セッションの相互敵対監査を台帳1本で回す | **(b) 新レール候補。最近縁 = Trust Without Trusting / blackboard architecture / ledger-state stigmergy** |
| [`three-layers-and-four-graphs`](institutions/three-layers-and-four-graphs.md) | 運転の3層と4つのグラフ | human-in / on-the-loop / human-in-command + control/knowledge/execution/improvement graph |
| [`pattern-catalog`](institutions/pattern-catalog.md) | 症状から確立された解法を引く台帳 | Pattern language (Alexander) + runbook / playbook |
| [`mental-models-canon`](institutions/mental-models-canon.md) | 人類の思考の型を体系化した読み物カノン | Latticework of mental models (Munger) + structured analytic techniques |
| [`oversight-metrics`](institutions/oversight-metrics.md) | 監督の質を週次で実測する | Override rate / rubber-stamp rate / HITL necessity rate |
| [`two-stage-check`](institutions/two-stage-check.md) | 上位が書き、安い別モデルが独立に検査する | Prover-Verifier Games (arXiv:2407.13692) + LLM-as-a-judge + blind review |
| [`risk-tiered-effort`](institutions/risk-tiered-effort.md) | リスク階層に応じて推論予算を配分する | Risk-based testing の graduated allocation + model cascade (FrugalGPT) |
| [`publication-registry`](institutions/publication-registry.md) | 置き場所ではなくファイル単位で公開物を判定する | DLP (NIST CSRC: identify, monitor, and protect data in use) + data classification |
| [`injection-is-not-compliance`](institutions/injection-is-not-compliance.md) | 注入と発火証明と遵守観測を3層に分ける | Instruction-following compliance rate (IFEval 系) + 「system prompt は control ではない」 |
| [`kill-switch-and-restore`](institutions/kill-switch-and-restore.md) | 一斉停止と一斉再開を対で1つの制度にする | Kill switch / emergency stop (EU AI Act Art.14(4)(e)) + state snapshot + restore/rollback runbook |
| [`question-catalog`](institutions/question-catalog.md) | 出典義務つきの問いカタログと回答の機械ゲート（skill `toi` の正本） | **(b) 新レール候補。最近縁 = structured analytic techniques / policy-enforced generation** |

## 件数

- skill 13本 ＋ 制度文書 21件 ＝ **34項目**
- 内訳: (a) 31 / (b) 3
- (b) の3件 = `toi`（正本 = `question-catalog`）/ `wiring-check` / `crosswatch`。いずれも最近縁の既存研究を名指しした上で差分を書いてある

## この表の作り方

各項目について「同じ運用単位が世界にあるか」を検索し、クエリ・ヒットの有無・採用した上流を記録した。
対訳が裏取りできなかったものは、その旨を項目側に明記してある（例: `l2package` の2軸索引の使い方）。
