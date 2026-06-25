# Before / After Gallery

# 前后对比索引

This page is the direct, README-friendly evidence index for the three Loop Anything before/after experiments.

本页是三组 Loop Anything 前后对比实验的直观证据索引，可直接从 README 引用。

## Quick result table / 快速结果表

| Case / 案例 | Before | After | Score delta | Loop status | Full evidence |
|---|---|---|---:|---|---|
| 01 Gaokao essay / 高考作文 | [baseline](../experiments/01-gaokao-essay/runs/control/output.md) | [Loop final](../experiments/01-gaokao-essay/runs/loop/final.md) | +21.8 | `full_pass` | [comparison](../experiments/01-gaokao-essay/evaluation/comparison.md) · [manifest](../experiments/01-gaokao-essay/runs/loop/loop-run-manifest.json) |
| 02 HTML aesthetic optimization / HTML 美学优化 | [baseline HTML](../experiments/02-landing-page/runs/control/output.html) | [Loop final HTML](../experiments/02-landing-page/runs/loop/final.html) | +32.7 | `full_pass` | [comparison](../experiments/02-landing-page/evaluation/comparison.md) · [manifest](../experiments/02-landing-page/runs/loop/loop-run-manifest.json) |
| 03 Receipt splitter reliability / 账单拆分工具可靠性 | [baseline](../experiments/03-receipt-splitter/runs/control/output.md) | [Loop final](../experiments/03-receipt-splitter/runs/loop/final.md) | +54.5 | `full_pass` | [comparison](../experiments/03-receipt-splitter/evaluation/comparison.md) · [manifest](../experiments/03-receipt-splitter/runs/loop/loop-run-manifest.json) |

## 01 Gaokao essay / 高考作文

### Direct document links / 直接文档链接

- Before full text / 前全文：[control output](../experiments/01-gaokao-essay/runs/control/output.md)
- After full text / 后全文：[Loop final](../experiments/01-gaokao-essay/runs/loop/final.md)
- Reviewer evidence / 审查证据：[reviewer outputs](../experiments/01-gaokao-essay/runs/loop/reviewers/)
- Detailed comparison / 详细对比：[comparison report](../experiments/01-gaokao-essay/evaluation/comparison.md)

### Side-by-side excerpt / 节选对比

| Before / Loop 前 | After / Loop 后 |
|---|---|
| 今天的世界变化很快，新词语、新技术、新生活方式不断出现，青年人也常常被鼓励去闯、去创新、去抵达更大的舞台。 | 可针线包提醒我，屏幕上的远方终究是别人的路线，不一定就是我的方向。我不再只问自己“是不是走得够快、够远”，也开始问“我为什么出发、凭什么站稳”。 |

**English conclusion:** The baseline connected the prompt to “the era” through a generic paragraph. The Loop version makes that connection concrete through the sewing kit, screen-mediated comparison, and the narrator’s changed understanding of “远方”.

**中文结论：** 原稿用泛化段落连接“时代变化”；Loop 后通过针线包、屏幕比较压力和“远方”的重新理解，把时代变化落到学生成长经验中。

**Loop status / Loop 状态:** `full_pass`. Final strict-grading, argument, and student-expression reviewers all returned `PASS 120`.

## 02 HTML aesthetic optimization / HTML 美学优化

### Direct artifact links / 直接产物链接

- Before full HTML / 前 HTML：[control output](../experiments/02-landing-page/runs/control/output.html)
- After full HTML / 后 HTML：[Loop final](../experiments/02-landing-page/runs/loop/final.html)
- Reviewer evidence / 审查证据：[reviewer outputs](../experiments/02-landing-page/runs/loop/reviewers/)
- Detailed comparison / 详细对比：[comparison report](../experiments/02-landing-page/evaluation/comparison.md)

### Visual comparison / 视觉对比

README display screenshots are available under [`../evidence/screenshots/`](../evidence/screenshots/):

- Before screenshot / 前截图：[`02-html-before-readme.png`](../evidence/screenshots/02-html-before-readme.png)
- After screenshot / 后截图：[`02-html-after-readme.png`](../evidence/screenshots/02-html-after-readme.png)

| Before / Loop 前 | After / Loop 后 |
|---|---|
| Real standalone HTML, usable and coherent, but visually conservative. Blue-gray palette, Arial/Helvetica typography, flat white cards, simple borders, basic loop SVG, and low brand distinctiveness. | Same core content, stronger aesthetics. Warm paper + dark hero stage, serif display type, cyan/violet/coral/gold identity, glass panel, glow, richer inline SVG, asymmetric Before/After cards, and more refined responsive rhythm. |

**English conclusion:** The baseline was not broken; it was a normal usable HTML page. The Loop version makes the same product content feel more distinctive, crafted, and product-worthy through visual design without relying on a larger product story.

**中文结论：** 原稿不是故意做差，而是正常可用的 HTML 页面。Loop 后在不扩写产品内容的前提下，通过视觉设计让同一套内容更有辨识度、完成度和产品质感。

## 03 Receipt splitter reliability / 账单拆分工具可靠性

### Direct document links / 直接文档链接

- Before result / 前结果：[control output](../experiments/03-receipt-splitter/runs/control/output.md)
- After result / 后结果：[Loop final](../experiments/03-receipt-splitter/runs/loop/final.md)
- Rules and tests / 规则与测试：[rules and test cases](../experiments/03-receipt-splitter/materials/rules-and-test-cases.md)
- Reviewer evidence / 审查证据：[reviewer outputs](../experiments/03-receipt-splitter/runs/loop/reviewers/)
- Detailed comparison / 详细对比：[comparison report](../experiments/03-receipt-splitter/evaluation/comparison.md)

### Side-by-side excerpt / 节选对比

| Before / Loop 前 | After / Loop 后 |
|---|---|
| Baseline result: 5/11 tests passed. It handled simple splits, item ownership, tax/tip allocation, and no-hidden-payer cases, but failed discount order, cent reconciliation, unknown people, empty split lists, negative prices, and invalid rates. | Loop final result: 11/11 tests passed. It applies discounts before tax/tip, keeps displayed cents adding up exactly, respects subset sharing, and rejects invalid receipt inputs clearly. |

**English conclusion:** The baseline was a plausible first draft, not a deliberately broken tool. It worked for easy receipt cases, but failed realistic money rules. The Loop final passed all named rules and edge cases.

**中文结论：** 原稿是看似正常的初稿，不是故意做坏的工具。它能处理简单账单，但会在真实金钱规则上出错。Loop 后通过所有命名规则和边界情况。

## Screenshot status / 截图状态

Experiment 02 includes README display screenshots in [`../evidence/screenshots/`](../evidence/screenshots/). The primary evidence remains the linked artifacts: full before outputs, full after outputs, reviewer outputs, per-case comparisons, scores, metrics, manifests, and the standalone HTML files for experiment 02.

实验 02 已在 [`../evidence/screenshots/`](../evidence/screenshots/) 提供 README 展示截图。主要证据仍是可点击产物：Loop 前全文、Loop 后全文、审查员输出、单组对比报告、评分、指标、manifest，以及实验 02 的单文件 HTML。

If additional screenshots are added later, keep them under [`../evidence/screenshots/`](../evidence/screenshots/) and link them from this page.

如果后续补充更多截图，请继续放到 [`../evidence/screenshots/`](../evidence/screenshots/) 并从本页链接。