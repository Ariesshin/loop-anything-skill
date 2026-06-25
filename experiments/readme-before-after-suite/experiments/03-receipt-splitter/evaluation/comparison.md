# Comparison

# 对比报告

## Case / 案例

Experiment 03 now evaluates **Receipt splitter reliability** / **账单拆分工具可靠性**.

It is designed for non-programmer-readable evidence: readers can inspect named money rules and a pass/fail table instead of reading code.

本实验三现在评估 **账单拆分工具可靠性**。它面向非程序员可读证据：读者看命名金钱规则和通过/失败表，而不是看代码。

## Scores / 分数

| Output | Passed tests | Raw score / 55 | Normalized score / 100 | Loop status |
|---|---:|---:|---:|---|
| Baseline | 5/11 | 25 | 45.5 | baseline |
| Loop final | 11/11 | 55 | 100.0 | full_pass |

## Before / After table / 前后对比表

| Test | Rule being checked | Before | After Loop | Plain-English result |
|---|---|---|---|---|
| T01 | simple equal split | PASS | PASS | Two people split one 10.00 item evenly. |
| T02 | item ownership | PASS | PASS | Each person pays only for their own item. |
| T03 | shared subset | PASS | PASS | Chen did not eat dessert and owes none of it. |
| T04 | tax and tip | PASS | PASS | Tax and tip follow each person's subtotal. |
| T05 | discount before tax/tip | FAIL — wrong amounts and total | PASS | The 4.00 discount is applied before tax and allocated proportionally. |
| T06 | rounding cents | FAIL — people sum 9.99 instead of total 10.00 | PASS | The extra cent goes to Alice because she is first in input order. |
| T07 | unknown person | FAIL — unclear `KeyError` | PASS | An item cannot charge someone outside the people list. |
| T08 | empty split list | FAIL — unclear `ZeroDivisionError` | PASS | Every item needs at least one payer. |
| T09 | negative price | FAIL — accepted invalid input | PASS | Negative item prices are rejected. |
| T10 | no hidden payer | PASS | PASS | Chen is on the bill but did not share the item, so Chen owes 0.00. |
| T11 | invalid rate | FAIL — accepted invalid input | PASS | Negative tax or tip rates are rejected. |

## What changed / 变化

- The baseline worked on easy cases but failed real receipt rules.
- baseline 能处理简单情况，但真实账单规则会出错。
- The final keeps the same task and same tests, but passes every named rule.
- final 保持同一任务和同一测试，但通过每条命名规则。
- The clearest human example: Chen did not eat dessert and should not pay for dessert; rounding cents must still make the displayed total add up exactly.
- 最直观的人话例子：Chen 没吃甜点就不应分摊甜点；分位取整后展示总额也必须正好对上。

## Loop review result / Loop 审查结果

Final reviewers:

- Rule correctness: `PASS 120`.
- Edge-case and reproducibility: `PASS 120`.
- README evidence readability: `PASS 120`.

Final status: `full_pass`.

## Reproduction / 复现

Baseline:

```bash
python3 experiments/readme-before-after-suite/experiments/03-receipt-splitter/materials/run_receipt_splitter_tests.py --impl experiments/readme-before-after-suite/experiments/03-receipt-splitter/runs/control/receipt_splitter.py --format markdown
```

Final:

```bash
python3 experiments/readme-before-after-suite/experiments/03-receipt-splitter/materials/run_receipt_splitter_tests.py --impl experiments/readme-before-after-suite/experiments/03-receipt-splitter/runs/loop/final.py --format markdown
```

## Limitations / 限制

- This is a small deterministic demonstration, not a broad software benchmark.
- 这是小型确定性演示，不是广泛软件基准。
- Scoring is based on the named T01–T11 test set.
- 评分基于命名的 T01–T11 测试集。
- Token usage is estimated from visible text only, not provider billing data.
- token 使用量只按可见文本估算，不是服务商账单数据。