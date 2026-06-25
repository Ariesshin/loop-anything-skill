# Experiment 02 Evidence Log

## Canonical artifacts

- Control: `runs/control/output.html`
- Loop v0: `runs/loop/v0.html`
- Loop final: `runs/loop/final.html`

Legacy markdown files are pointers only.

## Initial equality check

`runs/control/output.html` and `runs/loop/v0.html` were written from the same initial artifact before Loop revision.

Static validation confirms byte-for-byte equality:

- Control bytes: `16442`
- Loop v0 bytes: `16442`
- Control SHA256: `6d731e7178ace0d8742ca7443323f0e16487dfda5cb3f3c07df9b866a017e18c`
- Loop v0 SHA256: `6d731e7178ace0d8742ca7443323f0e16487dfda5cb3f3c07df9b866a017e18c`
- Equality result: `true`

## Final artifact checksum

- Final bytes: `38680`
- Final lines: `1234`
- Final SHA256: `0c3bd58ed6091c63502fe8ab6cc3de402e17b587a0ed42ebceb52b0b5e52ce87`

## Static HTML checks

- Complete standalone HTML document: present.
- `<!doctype html>`: present.
- `<html>`, `<head>`, `<style>`, `<body>`: present.
- Inline CSS: present.
- Inline SVG: present, `3` SVG elements.
- External image dependencies: none.
- External CSS or font dependencies: none.
- JavaScript framework imports: none.
- CDN dependencies: none.
- Browser-openability: static structure present; can be opened directly as a file.
- Visible CTA text: present.
- External HTTP references: GitHub CTA links only; no external asset dependencies.

## Content-change audit

Preserved major sections:

- Hero.
- Product explanation / what it does.
- Before / after intuition.
- How it works.
- Use cases.
- Tradeoff disclosure.
- Install target options.
- First request example.

Preserved product claims:

- 2-3 isolated AI reviewers.
- Different review angles.
- Review, revision, and repeated loop.
- `Score: 120` as zero-reservation stop signal.
- Use for important deliverables rather than every quick response.
- Higher time and estimated visible token tradeoff.
- Supported install targets from the source material.

CTA audit:

- Control and final both keep GitHub install CTA.
- Control and final both keep first-request/example CTA intent.
- CTA count and intent are preserved; visual treatment is upgraded.

Allowed wording changes:

- Section kickers and visual labels were added for layout rhythm and accessibility.
- No new feature, benchmark, pricing, customer, security, or platform guarantee claim was added.

## Aesthetic comparison notes

Baseline visual state:

- Usable, coherent, and browser-openable.
- Conservative blue-gray palette.
- Arial/Helvetica typography.
- Flat white cards with simple borders.
- Basic loop SVG and simple brand mark.
- Single broad responsive breakpoint.

Loop final visual state:

- Distinct warm paper + dark hero art direction.
- Cohesive cyan / violet / coral / gold color system.
- Serif display typography paired with system UI text.
- Gradient brand mark and richer inline SVG compositions.
- Stronger hero depth, glass panel, glow, shadows, and background grid.
- Before/After area now uses asymmetric card scale, desaturated dashed baseline card, glowing dark final card, and central gradient transition arrow.
- Section rhythm, button states, card hierarchy, and tablet/mobile timeline are visually refined.

## Screenshot status

Screenshot capture was not performed in this run. Direct HTML artifacts, static checks, text evidence, reviewer outputs, and manifest are used as fallback evidence.

## Loop review status

Final Loop reviewers:

- Art direction and visual identity: `PASS 120`
- Composition, typography, and spacing: `PASS 120`
- Single-file frontend craft: `PASS 120`

Final status: `full_pass`.