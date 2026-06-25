# Loop Round 1: Receipt splitter reliability

# Loop 第 1 轮：账单拆分工具可靠性

Round 1 changed the artifact from a plausible first draft into a rule-based receipt splitter:

第 1 轮把“看起来能用”的初稿改成了按规则执行的账单拆分工具：

- Tracks item ownership instead of relying on broad equal assumptions.
- 按菜品参与者分摊，而不是依赖粗略平分。
- Applies bill-level discount before tax/tip and allocates it proportionally.
- 整单折扣先于税和服务费，并按比例分摊。
- Allocates tax/tip proportionally after discount.
- 税和服务费按折扣后金额比例分摊。
- Reconciles displayed cents deterministically in input people order.
- 分位尾差按输入人员顺序确定性分配。
- Rejects unknown people, empty splits, negative prices, invalid rates, and oversized discounts.
- 明确拒绝未知人员、空分摊名单、负价格、非法税率/服务费率和过大折扣。

Round 1 implementation:

`runs/loop/round-1.py`

The same implementation was promoted to final after deterministic tests passed and final reviewers returned `PASS 120`.