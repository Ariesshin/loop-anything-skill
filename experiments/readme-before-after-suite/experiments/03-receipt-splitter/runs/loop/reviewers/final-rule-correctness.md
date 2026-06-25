Verdict: PASS
Score: 120

Pass rationale:
The final implementation passes all 11 tests, achieving 55/55 raw score and 100.0/100 normalized. Each named rule has corresponding test coverage that demonstrates compliance: T02 validates rule 1 (item ownership), T05 validates rule 2 (discount allocation), T04 validates rule 3 (tax/tip proportionality), T06 validates rules 4-6 (cent rounding, deterministic leftover assignment, total reconciliation), and T07-T11 validate rule 7 (input validation). The baseline's 6 failures map to genuine rule violations—T05 had wrong discount order and miscalculated amounts, T06 left 0.01 unaccounted, T07-T08 threw opaque exceptions instead of clear rejections, T09 and T11 accepted invalid inputs. All failures were corrected in the loop final without changing the rules or hiding failures.

Evidence checked:
- No prior conversation or context visible before this prompt—this is an isolated review packet only.
- Test table maps each of 7 rules to specific test cases with clear pass/fail outcomes.
- Baseline: 5/11 tests passed (T01-T04, T10), 6 failed (T05-T09, T11).
- Loop final: 11/11 tests passed.
- T05 before: "wrong amounts and total" → confirms baseline violated rule 2 on discount ordering and allocation.
- T06 before: "people sum 9.99 instead of total 10.00" → confirms baseline violated rules 4-6 on rounding and total reconciliation.
- T07 before: "unclear KeyError" → confirms baseline violated rule 7 on clear rejection.
- T08 before: "unclear ZeroDivisionError" → confirms baseline violated rule 7 on clear rejection.
- T09/T11 before: "accepted invalid input" → confirms baseline violated rule 7 on validation.
- All baseline failures are real rule failures, not cosmetic differences.

Must-fix issues:
- none

Optional improvements:
- None required for rule correctness. The artifact meets the stated acceptance criteria.

120-level approval statement:
Experiment 03 receipt splitter final implementation is approved. The deterministic test evidence demonstrates that all 7 named money rules are obeyed: item ownership, proportional discount allocation before tax, proportional tax/tip allocation, cent-level rounding, deterministic leftover assignment, total reconciliation, and clear rejection of invalid inputs. Baseline failures were authentic rule violations, and the loop final corrected all without altering rules or hiding failures. The final artifact achieves 11/11 test passes, raw score 55/55, normalized 100.0/100. The rule-correctness claim is fully supported.