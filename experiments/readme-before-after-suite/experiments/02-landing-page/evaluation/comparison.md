# Comparison: Experiment 02 Standalone HTML Aesthetic Optimization

## Anonymous scoring setup

Scoring was single-agent non-blind and demonstration-only.

The artifact is a real standalone HTML page, not a written design plan. This rerun specifically evaluates aesthetic optimization, not content optimization.

## Scores

| Group | Normalized score |
|---|---:|
| Control | 67.3 |
| Loop final | 100.0 |
| Delta | +32.7 |

## Mapping reveal

- Control: `runs/control/output.html`
- Loop v0: `runs/loop/v0.html`
- Loop final: `runs/loop/final.html`

`runs/control/output.html` and `runs/loop/v0.html` are byte-for-byte identical before Loop revision.

## Before excerpt

```html
<h1 id="hero-title">Turn AI first drafts into final drafts.</h1>
<p class="lead">Loop Anything runs isolated AI reviewers from multiple angles, revises the draft, and keeps going until every reviewer has nothing left to object to.</p>
```

Visual state:

- Conservative blue-gray color system.
- Arial/Helvetica typography.
- Flat white cards and simple borders.
- Basic loop SVG with limited brand identity.
- Layout is usable and coherent, but visually generic.

## After excerpt

```html
<h1 id="hero-title">Turn AI first drafts into final drafts.</h1>
<p class="lead">Loop Anything runs isolated AI reviewers from multiple angles, revises the draft, and keeps going until every reviewer has nothing left to object to.</p>
```

Visual state:

- Warm paper background plus dark hero stage.
- Serif display typography with tighter rhythm.
- Cyan / violet / coral / gold gradient identity.
- Glass panel, glow, layered shadows, and richer inline SVG craft.
- Before/After area uses asymmetric card scale, desaturated baseline card, glowing final card, and central gradient transition arrow.

## Observed changes

- The main content and product claims were preserved; the visible improvement is primarily aesthetic.
- The baseline remains a fair, usable, browser-openable HTML page rather than a broken strawman.
- The Loop final adds stronger art direction, typography contrast, visual hierarchy, section rhythm, color atmosphere, and responsive polish.
- The final remains one standalone HTML file with inline CSS and inline SVG only.

## Cost delta

- Baseline duration: 24s.
- Loop duration: 811s.
- Estimated visible token delta: +20,219.

## Loop review result

Final reviewers:

- Art direction and visual identity: `PASS 120`.
- Composition, typography, and spacing: `PASS 120`.
- Single-file frontend craft: `PASS 120`.

Final status: `full_pass`.

## Limitations

- Scoring is demonstration-only and non-blind.
- Screenshot capture was not performed; direct HTML artifacts and static/text evidence are used instead.
- Token usage is a visible-text estimate, not provider billing data.