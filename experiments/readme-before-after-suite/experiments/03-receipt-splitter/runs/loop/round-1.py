from __future__ import annotations

from decimal import Decimal, ROUND_FLOOR


CENT = Decimal("0.01")


def money(value) -> Decimal:
    return Decimal(str(value))


def cents_floor(value: Decimal) -> int:
    return int((value * 100).to_integral_value(rounding=ROUND_FLOOR))


def cents_to_string(value: int) -> str:
    return f"{Decimal(value) / 100:.2f}"


def validate(receipt: dict) -> tuple[list[str], list[dict], Decimal, Decimal, Decimal]:
    people = list(receipt.get("people", []))
    if not people:
        raise ValueError("people list is required")
    if len(set(people)) != len(people):
        raise ValueError("people list contains duplicates")

    items = list(receipt.get("items", []))
    discount = money(receipt.get("discount", "0.00"))
    tax_rate = money(receipt.get("tax_rate", "0.00"))
    tip_rate = money(receipt.get("tip_rate", "0.00"))

    if discount < 0:
        raise ValueError("discount cannot be negative")
    if tax_rate < 0 or tip_rate < 0:
        raise ValueError("tax_rate and tip_rate cannot be negative")

    known = set(people)
    for item in items:
        price = money(item.get("price", "0.00"))
        participants = list(item.get("participants", []))
        if price < 0:
            raise ValueError("item price cannot be negative")
        if not participants:
            raise ValueError("item participants cannot be empty")
        unknown = [name for name in participants if name not in known]
        if unknown:
            raise ValueError(f"unknown participant: {unknown[0]}")
        item["_price"] = price
        item["_participants"] = participants

    return people, items, discount, tax_rate, tip_rate


def reconcile(amounts: dict[str, Decimal], target: Decimal, people_order: list[str]) -> dict[str, str]:
    target_cents = int((target.quantize(CENT) * 100).to_integral_value())
    floors = {name: cents_floor(amounts[name]) for name in people_order}
    remainder = target_cents - sum(floors.values())
    for name in people_order:
        if remainder <= 0:
            break
        floors[name] += 1
        remainder -= 1
    return {name: cents_to_string(floors[name]) for name in people_order}


def split_receipt(receipt: dict) -> dict:
    people, items, discount, tax_rate, tip_rate = validate(receipt)

    subtotals = {person: Decimal("0.00") for person in people}
    for item in items:
        share = item["_price"] / Decimal(len(item["_participants"]))
        for person in item["_participants"]:
            subtotals[person] += share

    bill_subtotal = sum(subtotals.values())
    if bill_subtotal == 0:
        post_discount = {person: Decimal("0.00") for person in people}
        discount = Decimal("0.00")
    else:
        if discount > bill_subtotal:
            raise ValueError("discount cannot exceed subtotal")
        post_discount = {}
        for person in people:
            share = subtotals[person] / bill_subtotal
            post_discount[person] = subtotals[person] - discount * share

    total_after_discount = sum(post_discount.values())
    tax = total_after_discount * tax_rate
    tip = total_after_discount * tip_rate
    grand_total = total_after_discount + tax + tip

    exact = {}
    if total_after_discount == 0:
        for person in people:
            exact[person] = Decimal("0.00")
    else:
        for person in people:
            share = post_discount[person] / total_after_discount
            exact[person] = post_discount[person] + tax * share + tip * share

    displayed = reconcile(exact, grand_total, people)
    return {
        "people": displayed,
        "grand_total": f"{grand_total.quantize(CENT):.2f}",
    }