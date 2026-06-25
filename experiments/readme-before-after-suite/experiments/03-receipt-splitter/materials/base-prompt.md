# Base Prompt

Create a small Python receipt splitter for people sharing a restaurant bill.

The tool should accept:

- `people`: names on the bill.
- `items`: each item has a name, price, and participants who shared it.
- `discount`: a whole-bill discount.
- `tax_rate` and `tip_rate`.

Return a readable result showing each person's displayed amount and the displayed grand total.

The result should be useful for normal shared meals, not just equal splits.