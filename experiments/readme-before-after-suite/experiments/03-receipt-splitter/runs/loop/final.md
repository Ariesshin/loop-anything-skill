# Loop Final: Receipt splitter reliability

# Loop 最终版：账单拆分工具可靠性

## Artifact / 产物

Final implementation:

`runs/loop/final.py`

## Test command / 测试命令

```bash
python3 experiments/readme-before-after-suite/experiments/03-receipt-splitter/materials/run_receipt_splitter_tests.py --impl experiments/readme-before-after-suite/experiments/03-receipt-splitter/runs/loop/final.py --format markdown
```

## Result / 结果

Passed tests: 11/11

Raw score: 55/55

Normalized score: 100.0/100

| Test | Rule being checked | After Loop | Plain-English result |
|---|---|---|---|
| T01 | simple equal split | PASS | Two people split one 10.00 item evenly. |
| T02 | item ownership | PASS | Each person pays only for their own item. |
| T03 | shared subset | PASS | Chen did not eat dessert and owes none of it. |
| T04 | tax and tip | PASS | Tax and tip follow each person's subtotal. |
| T05 | discount before tax/tip | PASS | The 4.00 discount is applied before tax and allocated proportionally. |
| T06 | rounding cents | PASS | The extra cent goes to Alice because she is first in input order. |
| T07 | unknown person | PASS | An item cannot charge someone outside the people list. |
| T08 | empty split list | PASS | Every item needs at least one payer. |
| T09 | negative price | PASS | Negative item prices are rejected. |
| T10 | no hidden payer | PASS | Chen is on the bill but did not share the item, so Chen owes 0.00. |
| T11 | invalid rate | PASS | Negative tax or tip rates are rejected. |

## Plain conclusion / 人话结论

Before Loop, the tool looked fine on simple splits but failed real receipt rules. After Loop, every named rule and edge case in T01–T11 passed a reproducible test table.

Loop 前，小工具在简单平分时看起来没问题，但真实账单规则会出错；Loop 后，每条命名规则和边界情况都有可复现测试通过。