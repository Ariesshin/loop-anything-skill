# Comparison

## Anonymous scoring setup

Scoring mode: `single-agent non-blind scoring; demonstration only`.

The baseline and Loop final were scored after both outputs were saved. A fully blind scorer was not available in this run, so the result is treated as demonstration evidence, not an independent evaluation.

## Scores

| Output | Raw score / 55 | Normalized score / 100 | Notes |
|---|---:|---:|---|
| Baseline | 43 | 78.2 | Clear topic fit, but generic scene choice, weak era connection, and formulaic ending. |
| Loop final | 55 | 100.0 | Specific personal detail, clearer growth imprint, stronger era connection, and final reviewers all `PASS 120`. |

## Mapping reveal

- Output A: baseline
- Output B: Loop final

## Before excerpt

> 今天的世界变化很快，新词语、新技术、新生活方式不断出现，青年人也常常被鼓励去闯、去创新、去抵达更大的舞台。

## After excerpt

> 可针线包提醒我，屏幕上的远方终究是别人的路线，不一定就是我的方向。我不再只问自己“是不是走得够快、够远”，也开始问“我为什么出发、凭什么站稳”。

## Observed changes

- The baseline treats the era theme as a generic paragraph.
- The Loop final ties the era theme to a concrete student behavior: comparing with campus/travel content on a phone.
- The baseline uses a common “mother cooking / return home” scene.
- The Loop final uses a more specific object chain: classmate’s laundry note, mother’s sewing kit, spare buttons.
- The targeted rerun fixed the earlier argument gap by explicitly connecting the sewing kit to the narrator’s changed attitude toward chasing other people’s routes.
- Fresh final reviewers for strict grading, argument, and student expression all returned `PASS 120`.

## Cost delta

| Metric | Baseline | Loop | Delta |
|---|---:|---:|---:|
| Wall-clock seconds | 35 | 1260 | +1225 |
| Input chars | 400 | 68000 | +67600 |
| Output chars | 1141 | 25000 | +23859 |
| Estimated visible tokens | 386 | 23250 | +22864 |

Token numbers are estimates from visible text only, not billing token usage.

## Loop review result

Final reviewers:

- Strict grading: `PASS 120`.
- Argument: `PASS 120`.
- Student expression: `PASS 120`.

Final status: `full_pass`.

## Evidence note

The original five-round attempt is retained in reviewer history as failed evidence. The current `full_pass` claim is based on the targeted rerun and the fresh final reviewer outputs named `final-strict-grading.md`, `final-argument.md`, and `final-student-expression.md`.

## Limitations

- Gaokao scoring is not official scoring.
- Scoring is demonstration-only and non-blind.
- Experiment 01 is a text-only case; screenshots are not applicable. Text logs and saved reviewer outputs are the evidence.
