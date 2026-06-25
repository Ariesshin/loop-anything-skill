# Base Prompt: Loop Anything Standalone HTML Landing Page — Aesthetic Baseline

You are creating a real landing page for Loop Anything.

Source material:

Loop Anything is a skill that turns an AI first draft into a final draft. It runs 2-3 isolated AI reviewers, each reviewing the work from a different angle. Reviewers critique the work, the main agent revises, and the loop continues until every reviewer has nothing left to object to. `Score: 120` means that reviewer has zero remaining reservations. Anything below 120 triggers another revision round.

It works for important deliverables such as specs, proposals, difficult messages, job applications, system prompts, plans, and decisions. It trades more time and estimated visible tokens for higher confidence, so it is meant for the important 5% of outputs where being wrong is costly, not for every quick draft.

Supported install targets mentioned in the source material include Cursor, Claude Code, Codex, OpenCode, OpenClaw, ClawHub, and other platforms that can fetch the skill instructions.

Task:
Create one complete standalone HTML file for a Loop Anything landing page. The result must be a real single-file HTML artifact that can be opened directly in a browser.

Aesthetic baseline constraint:
Make the page usable and coherent, but visually conservative. Prioritize straightforward layout and basic styling over high-end art direction. Do not intentionally make it broken or ugly.

Hard constraints:

- Output only the complete HTML document.
- Use inline CSS and inline SVG only.
- Do not use external images.
- Do not use icon fonts.
- Do not use JavaScript frameworks.
- Do not use CDNs.
- Do not require a build step.
- Include a hero section, product explanation, before/after intuition, how it works, use cases, tradeoff disclosure, install CTA, and first request example.
- Keep product claims faithful to the source material.