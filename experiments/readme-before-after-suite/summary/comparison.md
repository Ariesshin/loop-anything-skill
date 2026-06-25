# Suite Comparison

# 实验汇总结论

## Status / 状态

Completed.

已完成。

- Scoring mode: `single-agent non-blind scoring; demonstration only`.
- 评分口径：`single-agent non-blind scoring; demonstration only`，仅作为演示评分。
- Token numbers: estimated from visible text only, not billing token usage.
- token 数字：只按可见文本估算，不是账单 token。
- Screenshot status: experiment 02 includes README display screenshots; saved logs, reviewer outputs, manifests, scores, HTML artifacts, and comparison files remain the canonical evidence.
- 截图状态：实验 02 已包含 README 展示截图；日志、审查员输出、manifest、评分、HTML 产物和对比文档仍是正式证据。

Direct before/after gallery: [`summary/before-after-gallery.md`](before-after-gallery.md)

直观前后对比索引：[`summary/before-after-gallery.md`](before-after-gallery.md)

## Cross-case summary / 三组结果汇总

| Experiment / 实验 | Baseline score | Loop score | Delta | Loop status | Baseline est. tokens | Loop est. tokens | Time delta |
|---|---:|---:|---:|---|---:|---:|---:|
| 01 Gaokao essay / 高考作文 | 78.2 | 100.0 | +21.8 | full_pass | 386 | 23,250 | +1225s |
| 02 HTML aesthetic optimization / HTML 美学优化 | 67.3 | 100.0 | +32.7 | full_pass | 4,587 | 24,806 | +787s |
| 03 Receipt splitter reliability / 账单拆分工具可靠性 | 45.5 | 100.0 | +54.5 | full_pass | 384 | 7,150 | +292s |

## Main conclusion / 主要结论

**English:** Across the three README-oriented cases, Loop Anything improved the recorded output quality, but at a clear cost in time and estimated visible tokens. Experiment 01 now reaches full Loop approval after a targeted rerun: the Gaokao essay turns a generic era paragraph into a concrete student growth argument with a clearer bridge between the sewing kit, screen-mediated comparison, and the changed meaning of “远方”. Experiment 02 specifically demonstrates aesthetic optimization of a real standalone HTML page: the same product content moves from a usable but visually conservative page to a polished page with stronger art direction, typography, color, composition, SVG craft, and responsive rhythm. Experiment 03 demonstrates small-tool reliability: a plausible receipt splitter first draft passes easy cases but fails real money rules, while the Loop final passes all named tests. All three runs reached full Loop approval (`PASS 120` from every final reviewer).

**中文：** 在三组面向 README 展示的案例中，Loop Anything 都带来了可记录的质量提升，但代价是更长耗时和更多估算可见 token。实验 01 经过针对性重跑后达到完整 Loop 通过：高考作文从泛化的时代段落，变成一条更具体的学生成长论证，针线包、屏幕比较压力和“远方”含义变化之间的桥更清楚。实验 02 明确展示真实单文件 HTML 的美学优化：同一套产品内容，从可用但视觉保守的页面，提升为更有艺术方向、排版、色彩、构图、SVG 工艺和响应式节奏的页面。实验 03 展示小工具可靠性：一个看似正常的账单拆分初稿能通过简单情况，但会在真实金钱规则上出错，Loop 后通过所有命名测试。三组实验均达到完整 Loop 通过（最终审查员全部 `PASS 120`）。

## README-ready excerpts / README 可引用节选

### 01 Gaokao essay / 高考作文

Links / 链接： [Before](../experiments/01-gaokao-essay/runs/control/output.md) · [After](../experiments/01-gaokao-essay/runs/loop/final.md) · [Comparison](../experiments/01-gaokao-essay/evaluation/comparison.md)

**Before:**

> 今天的世界变化很快，新词语、新技术、新生活方式不断出现，青年人也常常被鼓励去闯、去创新、去抵达更大的舞台。

**After:**

> 可针线包提醒我，屏幕上的远方终究是别人的路线，不一定就是我的方向。我不再只问自己“是不是走得够快、够远”，也开始问“我为什么出发、凭什么站稳”。

**English conclusion:** Generic era paragraph became a concrete student growth argument: the sewing kit changes the narrator’s attitude toward screen-mediated comparison and the changed meaning of “远方”.

**中文结论：** 泛化的时代段落变成了具体学生成长论证：针线包让“我”重新看待屏幕里的比较压力，也推动“远方”一词含义变化。

**Loop status / Loop 状态:** `full_pass`. Final strict-grading, argument, and student-expression reviewers all returned `PASS 120`.

### 02 HTML aesthetic optimization / HTML 美学优化

Links / 链接： [Before HTML](../experiments/02-landing-page/runs/control/output.html) · [After HTML](../experiments/02-landing-page/runs/loop/final.html) · [Comparison](../experiments/02-landing-page/evaluation/comparison.md)

**Before visual state:** usable standalone HTML, conservative blue-gray palette, Arial/Helvetica typography, flat white cards, simple SVG, basic visual identity.

**Loop final visual state:** same core content, but upgraded with warm paper + dark hero art direction, serif display typography, cyan/violet/coral/gold identity, glass panel, glow, richer inline SVG, asymmetric Before/After cards, and responsive visual rhythm.

**English conclusion:** The final did not win by rewriting the product story. It won by making the same browser-openable HTML artifact aesthetically stronger and more product-worthy.

**中文结论：** 这个最终版不是靠重写产品故事取胜，而是把同一份可浏览器打开的 HTML 产物做得更有审美完成度和产品质感。

### 03 Receipt splitter reliability / 账单拆分工具可靠性

Links / 链接： [Before](../experiments/03-receipt-splitter/runs/control/output.md) · [After](../experiments/03-receipt-splitter/runs/loop/final.md) · [Comparison](../experiments/03-receipt-splitter/evaluation/comparison.md) · [Rules and tests](../experiments/03-receipt-splitter/materials/rules-and-test-cases.md)

**Before:**

> Baseline result: 5/11 tests passed. It handled simple splits, item ownership, tax/tip allocation, and no-hidden-payer cases, but failed discount order, cent reconciliation, unknown people, empty split lists, negative prices, and invalid rates.

**After:**

> Loop final result: 11/11 tests passed. It applies discounts before tax/tip, keeps displayed cents adding up exactly, respects subset sharing, and rejects invalid receipt inputs clearly.

**English conclusion:** This case shows that Loop does not only polish words or visuals; it can make a small tool obey clear real-world rules.

**中文结论：** 这个案例说明 Loop 不只是润色文字或优化视觉；它也能让小工具遵守清晰的现实规则。

## Evidence links / 证据链接

- Before/After gallery / 前后对比索引：[`summary/before-after-gallery.md`](before-after-gallery.md)
- Method / 方法：[`materials/method.md`](../materials/method.md)
- Sources / 来源：[`materials/sources.md`](../materials/sources.md)
- Scores / 评分：[`summary/scores.csv`](scores.csv)
- Metrics / 指标：[`summary/metrics.json`](metrics.json)
- 01 comparison / 01 对比：[`experiments/01-gaokao-essay/evaluation/comparison.md`](../experiments/01-gaokao-essay/evaluation/comparison.md)
- 02 comparison / 02 对比：[`experiments/02-landing-page/evaluation/comparison.md`](../experiments/02-landing-page/evaluation/comparison.md)
- 03 comparison / 03 对比：[`experiments/03-receipt-splitter/evaluation/comparison.md`](../experiments/03-receipt-splitter/evaluation/comparison.md)
- 01 manifest：[`experiments/01-gaokao-essay/runs/loop/loop-run-manifest.json`](../experiments/01-gaokao-essay/runs/loop/loop-run-manifest.json)
- 02 manifest：[`experiments/02-landing-page/runs/loop/loop-run-manifest.json`](../experiments/02-landing-page/runs/loop/loop-run-manifest.json)
- 03 manifest：[`experiments/03-receipt-splitter/runs/loop/loop-run-manifest.json`](../experiments/03-receipt-splitter/runs/loop/loop-run-manifest.json)

## Limitations / 限制

- Demonstration suite only; not a statistically significant study.
- 这是演示实验，不是统计显著的学术研究。
- Gaokao scoring is not official scoring.
- 高考作文评分不是官方阅卷结果。
- All three runs reached full Loop approval.
- 三组实验均达到完整 Loop 通过。
- Token usage is estimated from visible text only.
- token 使用量仅为可见文本估算。
- Experiment 02 includes README display screenshots; text and static HTML artifacts remain the canonical evidence.
- 实验 02 已包含 README 展示截图；文本和静态 HTML 产物仍是正式证据。