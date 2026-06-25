# Method

## Purpose

This suite tests whether Loop Anything creates visible quality improvements over a single-pass AI draft in three README-ready scenarios:

1. A real 2026 Gaokao essay prompt.
2. A real standalone HTML aesthetic-optimization landing page for Loop Anything.
3. A receipt splitter reliability case for Loop Anything.

The goal is demonstration evidence for README before/after examples, not statistically significant academic proof.

## Group design

Each experiment follows the same split:

1. Use one fixed base prompt and fixed source material.
2. Generate one single-pass AI output.
3. Save that output as the control group baseline.
4. Use the exact same output as the Loop group `v0`.
5. Apply Loop Anything review and revision to create the treatment group final output.
6. Score baseline and Loop final with the same rubric.

This controls for random differences between two separate first drafts. The comparison is: same draft, without Loop vs with Loop.

## Base prompt policy

Base prompts must describe the task, source material, artifact constraints, target audience, and delivery boundary only.

They must not include scoring language such as `specificity`, `template risk`, `CTA clarity`, `visual hierarchy`, or similar rubric terms unless the task itself cannot be stated without them.

Product experiments need source context because the model cannot design or write about Loop Anything without product material. This is not cross-experiment symmetry; it is task input. The within-experiment split remains fair because baseline and Loop `v0` use the exact same prompt and initial output.

## Loop stopping criteria

Each Loop treatment run stops at the earliest of:

1. all selected reviewers return `PASS` with `Score: 120`;
2. five review rounds are completed;
3. the same must-fix issue recurs twice without new actionable detail;
4. the model/tooling fails twice on the same required operation.

If stopping condition 2-4 occurs, the run is marked `blocked` or `not_full_pass`; the report must not claim full Loop approval.

## Shared metrics

Each run records:

- `model_label`: visible runtime model label when available.
- `start_time` and `end_time`: wall-clock timestamps.
- `duration_seconds`: wall-clock elapsed time.
- `input_chars` and `output_chars`.
- `token_estimate`: visible-text estimate only.
- `token_estimate_note`: always states that this is not billing token usage.
- `loop_rounds`: for Loop runs only.
- `reviewer_count`: for Loop runs only.
- `final_loop_status`: PASS/REVISE/blocked.

## Token accounting

Token numbers in this suite are estimates.

They include visible prompts, visible outputs, reviewer packets, reviewer outputs, and revision artifacts when available.

They do not include hidden system prompts, tool schemas, provider-side routing, invisible cache behavior, or billable accounting from the model provider.

Every token number must be reported as `estimated`, not exact billing data.

## Scoring protocol

Scoring is done after both baseline and Loop final are saved.

To reduce expectation bias:

1. Baseline and Loop final are copied into anonymous scoring packets as `Output A` and `Output B`.
2. The scorer applies the same rubric without seeing which output is baseline or Loop.
3. After scores are recorded, the mapping is revealed in `evaluation/comparison.md`.

If blind scoring cannot be performed because the same agent generated and evaluates the outputs, the report must state: `single-agent non-blind scoring; demonstration only`.

## Score normalization

Each experiment has 11 dimensions:

- 6 shared dimensions.
- 5 domain-specific dimensions.

Each dimension is scored 0-5, for a raw maximum of 55.

Normalized score:

`normalized_score_100 = round(raw_score / 55 * 100, 1)`

Loop reviewer scores remain separate from output quality scores:

- reviewer score: 0-120, used only for Loop approval.
- output quality score: 0-100 normalized, used for baseline vs Loop comparison.

## Shared scoring rubric

Each output receives 0-5 points on the shared dimensions:

- Task fit.
- Concrete detail.
- Audience fit.
- Structure clarity.
- Deliverability.
- Low genericness, where higher means less generic.

Each experiment also has domain-specific dimensions.

## Experiment 01: Gaokao essay rubric

Additional 0-5 dimensions:

- Accurate response to the prompt.
- Clear change in understanding of one word.
- Credible growth imprint.
- Argument support.
- Compliance with Gaokao constraints.

## Experiment 02: standalone HTML aesthetic-optimization rubric

Experiment 02 is evaluated as a real browser-openable HTML artifact, not as a written design plan.

The experiment specifically tests aesthetic optimization: the control page is usable and coherent but visually conservative, while the Loop final should preserve the same core content and product claims but improve art direction, typography, layout rhythm, color, material treatment, inline SVG craft, and responsive visual polish.

Additional 0-5 dimensions:

- Art direction and visual identity.
- Typography and hierarchy.
- Layout composition and rhythm.
- Color, contrast, and atmosphere.
- Responsive aesthetic craft.

Canonical artifacts:

- `runs/control/output.html`
- `runs/loop/v0.html`
- `runs/loop/final.html`

The legacy markdown files in experiment 02 are kept only as pointers to the canonical HTML artifacts.

## Experiment 03: receipt splitter reliability rubric

Experiment 03 is evaluated as a small-tool reliability artifact, not as copy polishing.

The experiment uses a deterministic receipt-splitting rule set and T01-T11 tests. The baseline is a plausible first draft that handles simple cases but remains unstable around real money rules. The Loop final must preserve the same rules and tests while improving correctness, edge-case handling, and non-programmer-readable evidence.

Additional 0-5 dimensions:

- Correct item ownership and subset sharing.
- Discount-before-tax/tip order.
- Tax/tip allocation by adjusted subtotal.
- Exact cent reconciliation.
- Clear invalid-input rejection.

Canonical artifacts:

- `runs/control/receipt_splitter.py`
- `runs/loop/v0.py`
- `runs/loop/round-1.py`
- `runs/loop/final.py`
- `materials/rules-and-test-cases.md`
- `materials/run_receipt_splitter_tests.py`

The markdown files in experiment 03 are human-readable result summaries and evidence pointers for the canonical Python artifacts.

## Manifest schema

Each Loop run writes `runs/loop/loop-run-manifest.json` with:

```json
{
  "experiment_id": "01-gaokao-essay",
  "artifact_type": "essay|standalone_html_landing_page_aesthetic_optimization|receipt_splitter_reliability",
  "model_label": "runtime-visible model label",
  "runtime_platform": "Cursor agent",
  "isolation_confirmed": true,
  "degraded": false,
  "start_time": "ISO-8601",
  "end_time": "ISO-8601",
  "duration_seconds": 0,
  "input_chars": 0,
  "output_chars": 0,
  "loop_rounds": 0,
  "reviewer_count": 0,
  "facets": [
    {
      "name": "facet name",
      "mission": "what it protects",
      "final_verdict": "PASS|REVISE",
      "final_score": 120,
      "reviewer_output_path": "runs/loop/reviewers/..."
    }
  ],
  "rounds": [
    {
      "round": 1,
      "reviewer_outputs": ["runs/loop/reviewers/round-1-...md"],
      "revision_path": "runs/loop/round-1.md"
    }
  ],
  "final_loop_status": "full_pass|not_full_pass|blocked",
  "token_estimate": {
    "input_visible_estimate": 0,
    "output_visible_estimate": 0,
    "total_visible_estimate": 0,
    "note": "Estimated from visible text only; not billing token usage."
  }
}
```

`degraded: true` means isolated reviewer execution was unavailable and the run used sequential same-agent review. A degraded run must not be described as full isolated Loop approval.

## Comparison structure

Each `evaluation/comparison.md` uses this structure:

```markdown
# Comparison

## Anonymous scoring setup

## Scores

## Mapping reveal

## Before excerpt

## After excerpt

## Observed changes

## Cost delta

## Limitations
```

## Execution phase boundary

The suite has two phases:

1. Method/material review before experiments run.
2. Experiment execution after method approval.

During phase 1, placeholder result files may contain `TBD` or `pending_experiment_execution`. That is expected. Method approval only checks whether the materials, controls, templates, evidence policy, directory structure, and replay path are complete enough to run.

During phase 2, every placeholder result file must be replaced by the actual control output, Loop v0, Loop final, reviewer outputs, metrics, scores, comparison notes, and logs or screenshots.

## Evidence policy

Required evidence:

- Full baseline output.
- Full Loop `v0`.
- Full Loop final output.
- Reviewer outputs.
- Metrics JSON for each group.
- Score CSV and comparison notes.

Global evidence under `evidence/` is for suite-level screenshots and logs. Per-experiment `evidence/` is for experiment-specific screenshots and logs.

Screenshot evidence is useful when it captures visible runtime facts, final report pages, or review results. If UI screenshots are unavailable, text logs are acceptable and the limitation must be stated.

## Claims allowed

Allowed:

- In this suite, Loop produced the recorded differences.
- Loop cost more time and estimated tokens than the single-pass output.
- Specific weaknesses in the baseline were addressed in the Loop final.

Not allowed:

- Loop Anything is universally better.
- These scores equal official Gaokao scoring.
- Estimated token usage equals billable token usage.
- A single run proves statistical significance.