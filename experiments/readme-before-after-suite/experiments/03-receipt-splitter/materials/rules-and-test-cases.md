# Receipt Splitter Rules and Test Cases

# 账单拆分规则与测试用例

## Public case label / 公开案例名称

- English: `Receipt splitter reliability`
- 中文：`账单拆分工具可靠性`

## Human-readable rules / 人话规则

The receipt splitter receives:

工具输入：

- `people`: the people on the bill.
- `items`: each item has a price and a list of people who shared it.
- `discount`: a bill-level discount applied before tax and tip.
- `tax_rate` and `tip_rate`.

The tool must follow these rules:

1. Only people listed on an item pay for that item.
2. Bill-level discount is allocated in proportion to each person's item subtotal.
3. Tax and tip are allocated in proportion to each person's post-discount subtotal.
4. Every displayed result is rounded to cents.
5. Rounding leftovers are assigned deterministically in input `people` order.
6. Displayed person totals must add up exactly to the displayed grand total.
7. Unknown people, empty participant lists, negative prices, and invalid rates must be rejected clearly.

## Deterministic tests / 确定性测试

| Test | Rule being checked | Expected outcome |
|---|---|---|
| T01 simple equal split | Two people split one item, no tax/tip | Alice 5.00, Bob 5.00, total 10.00 |
| T02 item ownership | People pay only for their own items | Alice 12.00, Bob 8.00, total 20.00 |
| T03 shared subset | A person who did not share dessert pays none of it | Alice 4.50, Bob 4.50, Chen 0.00, total 9.00 |
| T04 tax and tip | Tax/tip follow each person's subtotal | Alice 26.00, Bob 39.00, total 65.00 |
| T05 discount before tax/tip | Discount lowers subtotal before tax | Alice 29.70, Bob 9.90, total 39.60 |
| T06 rounding cents | Uneven cents still sum exactly | Alice 3.34, Bob 3.33, Chen 3.33, total 10.00 |
| T07 unknown person | Item references someone not on people list | clear error |
| T08 empty split list | Item has no payer | clear error |
| T09 negative price | Price below zero | clear error |
| T10 no hidden payer | Person with no items owes 0.00 | Alice 6.00, Bob 6.00, Chen 0.00, total 12.00 |
| T11 invalid rate | Tax or tip rate is invalid | clear error |

## Scoring / 评分

The deterministic test score is 5 points per test:

确定性测试分每项 5 分：

- max raw score: 55.
- normalized score: `raw_score / 55 * 100`, rounded to one decimal.

This is demonstration evidence only, not a statistically significant benchmark.