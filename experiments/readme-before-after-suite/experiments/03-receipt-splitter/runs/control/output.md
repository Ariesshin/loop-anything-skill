# Control Output: Receipt splitter reliability

# 对照组输出：账单拆分工具可靠性

## Artifact / 产物

Baseline implementation:

`runs/control/receipt_splitter.py`

This is a plausible first-draft receipt splitter. It handles simple shared meals, item ownership, and tax/tip on basic cases, but it is unreliable on discount order, cent reconciliation, and invalid inputs.

这是一个看起来合理的初稿账单拆分工具。它能处理简单分摊、菜品归属和基础税费场景，但在折扣顺序、分位对账和非法输入上不可靠。

## Test command / 测试命令

```bash
python3 experiments/readme-before-after-suite/experiments/03-receipt-splitter/materials/run_receipt_splitter_tests.py --impl experiments/readme-before-after-suite/experiments/03-receipt-splitter/runs/control/receipt_splitter.py --format markdown
```

## Result / 结果

Passed tests: 5/11

Raw score: 25/55

Normalized score: 45.5/100

| Test | Rule being checked | Before | Plain-English result |
|---|---|---|---|
| T01 | simple equal split | PASS | Two people split one 10.00 item evenly. |
| T02 | item ownership | PASS | Each person pays only for their own item. |
| T03 | shared subset | PASS | Chen did not eat dessert and owes none of it. |
| T04 | tax and tip | PASS | Tax and tip follow each person's subtotal. |
| T05 | discount before tax/tip | FAIL — Alice 31.00 / Bob 9.00, total 40.00 instead of Alice 29.70 / Bob 9.90, total 39.60 | The tool applies discount in the wrong way. |
| T06 | rounding cents | FAIL — people sum 9.99 instead of total 10.00 | The extra cent is not reconciled to Alice. |
| T07 | unknown person | FAIL — unclear `KeyError` | Unknown people are not rejected clearly. |
| T08 | empty split list | FAIL — unclear `ZeroDivisionError` | Empty item participants are not rejected clearly. |
| T09 | negative price | FAIL — accepted invalid input | Negative item prices are not rejected. |
| T10 | no hidden payer | PASS | Chen is on the bill but did not share the item, so Chen owes 0.00. |
| T11 | invalid rate | FAIL — accepted invalid input | Negative tax or tip rates are not rejected. |

## Plain conclusion / 人话结论

The baseline is not useless. It works on easy cases. The problem is reliability: once a real receipt has discount order, rounding cents, or invalid inputs, the result can be wrong or unclear.

baseline 不是完全不能用。它能处理简单场景。问题是可靠性：一旦真实账单涉及折扣顺序、分位对账或非法输入，结果就可能错误或不清楚。