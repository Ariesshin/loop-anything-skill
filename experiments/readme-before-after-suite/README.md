# README Before / After Suite

# README 前后对比实验套件

## Purpose / 目的

This suite records three controlled before/after experiments for Loop Anything:

本套件记录了三组 Loop Anything 控制实验：

1. A real 2026 National I Gaokao essay prompt. / 真实 2026 全国 I 卷高考作文题。
2. A real standalone HTML aesthetic optimization case for Loop Anything. / Loop Anything 真实单文件 HTML 美学优化案例。
3. A receipt splitter reliability case for Loop Anything. / Loop Anything 账单拆分工具可靠性案例。

These are README-worthy demonstrations, not user instructions and not statistically significant proof.

这些是可放进 README 的展示型实验，不是用户教程，也不是统计显著证明。

## Direct Before / After gallery / 直观前后对比入口

Open this first if you want the clearest comparison:

如果你想直接看前后差异，先打开这个文件：

- [`summary/before-after-gallery.md`](summary/before-after-gallery.md)

It includes:

其中包含：

- Direct links to every full Before and After artifact. / 每组 Loop 前、Loop 后完整产物链接。
- Side-by-side excerpts. / 并排节选对比。
- Score deltas and Loop status. / 分数变化和 Loop 状态。
- Links to reviewer evidence, manifests, and detailed comparison reports. / 审查员输出、manifest 和详细对比报告链接。

## Method status / 方法状态

- Token policy: estimated visible-text tokens only, not billing data.
- token 口径：只估算可见文本 token，不是账单数据。
- Scoring policy: `single-agent non-blind scoring; demonstration only`.
- 评分口径：`single-agent non-blind scoring; demonstration only`，仅作演示评分。
- Screenshot policy: experiment 02 includes README display screenshots; saved logs, reviewer outputs, manifests, scores, HTML artifacts, and comparison files remain the canonical evidence.
- 截图口径：实验 02 已包含 README 展示截图；日志、审查员输出、manifest、评分、HTML 产物和对比文档仍是正式证据。

## Result summary / 结果汇总

| Experiment / 实验 | Baseline score | Loop score | Quality delta | Baseline duration | Loop duration | Estimated token delta | Loop status |
|---|---:|---:|---:|---:|---:|---:|---|
| 01 Gaokao essay / 高考作文 | 78.2 | 100.0 | +21.8 | 35s | 1260s | +22,864 | full_pass |
| 02 HTML aesthetic optimization / HTML 美学优化 | 67.3 | 100.0 | +32.7 | 24s | 811s | +20,219 | full_pass |
| 03 Receipt splitter reliability / 账单拆分工具可靠性 | 45.5 | 100.0 | +54.5 | 26s | 318s | +6,766 | full_pass |

## Main conclusion / 主要结论

**English:** Loop Anything improved all three recorded outputs, but with higher time and estimated visible-token cost. Experiment 01 now reaches full Loop approval after a targeted rerun: the Gaokao essay moves from a generic era paragraph to a concrete student growth story with a clear argument bridge. Experiment 02 specifically demonstrates aesthetic optimization of a real single-file HTML page: the same product content moved from a usable but visually conservative page to a more distinctive, crafted, product-worthy interface. Experiment 03 demonstrates small-tool reliability: a plausible receipt splitter first draft passed simple cases, while the Loop final passed every named money rule and edge case. All three experiments reached full Loop approval.

**中文：** Loop Anything 在三组实验中都带来了记录内的质量提升，但代价是更长耗时和更多估算可见 token。实验 01 经过针对性重跑后达到完整 Loop 通过：高考作文从泛化的时代段落，变成有具体学生成长细节和清晰论证桥的文章。实验 02 明确展示真实单文件 HTML 的美学优化：同一套产品内容，从可用但视觉保守的页面，提升为更有辨识度、完成度和产品质感的界面。实验 03 展示小工具可靠性：一个看似正常的账单拆分初稿只能通过简单情况，Loop 后通过每条明确金钱规则和边界情况。三组实验均达到完整 Loop 通过。

## README-ready excerpts / README 可引用节选

### 01 Gaokao essay / 高考作文

Links / 链接： [Before](experiments/01-gaokao-essay/runs/control/output.md) · [After](experiments/01-gaokao-essay/runs/loop/final.md) · [Comparison](experiments/01-gaokao-essay/evaluation/comparison.md)

**Before:**

> 今天的世界变化很快，新词语、新技术、新生活方式不断出现，青年人也常常被鼓励去闯、去创新、去抵达更大的舞台。

**After:**

> 可针线包提醒我，屏幕上的远方终究是别人的路线，不一定就是我的方向。我不再只问自己“是不是走得够快、够远”，也开始问“我为什么出发、凭什么站稳”。

**English conclusion:** Generic era-language became a concrete student growth argument: the sewing kit changes the narrator’s attitude toward screen-mediated comparison and the meaning of “远方”.

**中文结论：** 泛化的时代段落变成了具体学生成长论证：针线包让“我”重新看待屏幕里的比较压力，也推动“远方”一词含义变化。

**Loop status / Loop 状态:** `full_pass`. Final strict-grading, argument, and student-expression reviewers all returned `PASS 120`.

### 02 HTML aesthetic optimization / HTML 美学优化

Links / 链接： [Before HTML](experiments/02-landing-page/runs/control/output.html) · [After HTML](experiments/02-landing-page/runs/loop/final.html) · [Comparison](experiments/02-landing-page/evaluation/comparison.md)

**Before visual state:**

Usable standalone HTML with the same core product content, but visually conservative: blue-gray palette, Arial/Helvetica typography, flat white cards, simple borders, basic loop SVG, and limited brand distinctiveness.

**Loop final visual state:**

Same core content, stronger visual craft: warm paper background, dark hero stage, serif display type, cyan/violet/coral/gold identity, glass panel, glow, richer inline SVG, asymmetric Before/After cards, and more refined responsive rhythm.

**English conclusion:** This case now evaluates HTML aesthetics directly. The baseline was a fair, usable page; the Loop final made the same product content feel more distinctive, crafted, and product-worthy through visual design.

**中文结论：** 这个案例现在直接评估 HTML 美学效果。原稿是公平、可用的页面；Loop 后在保持同一套产品内容的前提下，通过视觉设计提升辨识度、完成度和产品质感。

**Loop status / Loop 状态:** `full_pass`.

### 03 Receipt splitter reliability / 账单拆分工具可靠性

Links / 链接： [Before](experiments/03-receipt-splitter/runs/control/output.md) · [After](experiments/03-receipt-splitter/runs/loop/final.md) · [Comparison](experiments/03-receipt-splitter/evaluation/comparison.md) · [Rules and tests](experiments/03-receipt-splitter/materials/rules-and-test-cases.md)

**Before:**

> Baseline result: 5/11 tests passed. It handled simple splits, item ownership, tax/tip allocation, and no-hidden-payer cases, but failed discount order, cent reconciliation, unknown people, empty split lists, negative prices, and invalid rates.

**After:**

> Loop final result: 11/11 tests passed. It applies discounts before tax/tip, keeps displayed cents adding up exactly, respects subset sharing, and rejects invalid receipt inputs clearly.

**English conclusion:** This case shows that Loop does not only polish words or visuals; it can make a small tool obey clear real-world rules.

**中文结论：** 这个案例说明 Loop 不只是润色文字或优化视觉；它也能让小工具遵守清晰的现实规则。

**Loop status / Loop 状态:** `full_pass`. Final rule-correctness, edge-case reproducibility, and README-evidence-readability reviewers all returned `PASS 120`.

## Evidence index / 证据索引

- Before/After gallery / 前后对比索引：`summary/before-after-gallery.md`
- Sources / 来源：`materials/sources.md`
- Method / 方法：`materials/method.md`
- Scores / 评分：`summary/scores.csv`
- Metrics / 指标：`summary/metrics.json`
- Suite comparison / 汇总对比：`summary/comparison.md`
- Evidence log / 证据日志：`evidence/logs/run-evidence.md`
- Screenshots directory / 截图目录：`evidence/screenshots/`
- 01 comparison / 01 对比：`experiments/01-gaokao-essay/evaluation/comparison.md`
- 02 comparison / 02 对比：`experiments/02-landing-page/evaluation/comparison.md`
- 03 comparison / 03 对比：`experiments/03-receipt-splitter/evaluation/comparison.md`
- 01 manifest：`experiments/01-gaokao-essay/runs/loop/loop-run-manifest.json`
- 02 manifest：`experiments/02-landing-page/runs/loop/loop-run-manifest.json`
- 03 manifest：`experiments/03-receipt-splitter/runs/loop/loop-run-manifest.json`

## Limitations / 限制

- Demonstration suite only; not a statistically significant study.
- 这是演示实验，不是统计显著的学术研究。
- Gaokao prompt source is real, but scoring is not official scoring.
- 高考题源真实，但评分不是官方阅卷结果。
- Token usage is estimated from visible text only, not provider billing data.
- token 使用量只按可见文本估算，不是服务商账单数据。
- All recorded final runs reached full Loop approval.
- 三组最终产物均达到完整 Loop 通过。
- Experiment 02 includes README display screenshots; text artifacts, static HTML, reviewer outputs, and manifests remain the canonical evidence.
- 实验 02 已包含 README 展示截图；文本产物、静态 HTML、审查员输出和 manifest 仍是正式证据。