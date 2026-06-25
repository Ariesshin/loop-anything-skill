# Evidence Log

Experiment 02 includes README display screenshots under `evidence/screenshots/`. Text artifacts, static HTML files, reviewer outputs, manifests, scores, and comparison files remain the canonical evidence according to `materials/method.md`.

实验 02 已在 `evidence/screenshots/` 提供 README 展示截图。根据 `materials/method.md`，文本产物、静态 HTML、审查员输出、manifest、评分和对比文档仍是正式证据。

Most direct visual/index entry:

最直观的前后对比入口：

- `summary/before-after-gallery.md`

Evidence saved:

- Base prompts: `experiments/*/materials/base-prompt.md`
- 01 control output: `experiments/01-gaokao-essay/runs/control/output.md`
- 02 control HTML aesthetic baseline: `experiments/02-landing-page/runs/control/output.html`
- 03 control output: `experiments/03-receipt-splitter/runs/control/output.md`
- 01/03 Loop v0 outputs: `experiments/01-gaokao-essay/runs/loop/v0.md`, `experiments/03-receipt-splitter/runs/loop/v0.md`
- 02 Loop v0 HTML: `experiments/02-landing-page/runs/loop/v0.html`
- 01/03 Loop final outputs: `experiments/01-gaokao-essay/runs/loop/final.md`, `experiments/03-receipt-splitter/runs/loop/final.md`
- 02 Loop final aesthetic HTML: `experiments/02-landing-page/runs/loop/final.html`
- Reviewer outputs: `experiments/*/runs/loop/reviewers/*.md`
- Loop manifests: `experiments/*/runs/loop/loop-run-manifest.json`
- Per-experiment scores: `experiments/*/evaluation/scores.csv`
- Per-experiment comparisons: `experiments/*/evaluation/comparison.md`
- Suite scores: `summary/scores.csv`
- Suite metrics: `summary/metrics.json`
- Suite comparison: `summary/comparison.md`

Token usage note:

All token numbers are estimated from visible text only and are not billing token usage.