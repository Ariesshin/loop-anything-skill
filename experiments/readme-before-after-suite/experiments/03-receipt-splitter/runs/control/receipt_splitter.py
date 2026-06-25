from __future__ import annotations


def split_receipt(receipt: dict) -> dict:
    people = list(receipt.get("people", []))
    items = list(receipt.get("items", []))
    discount = float(receipt.get("discount", 0))
    tax_rate = float(receipt.get("tax_rate", 0))
    tip_rate = float(receipt.get("tip_rate", 0))

    if not people:
        raise ValueError("people list is required")

    totals = {person: 0.0 for person in people}
    for item in items:
        participants = list(item.get("participants", []))
        share = float(item.get("price", 0)) / len(participants)
        for person in participants:
            totals[person] += share

    for person in people:
        totals[person] = totals[person] + totals[person] * tax_rate + totals[person] * tip_rate

    if discount:
        per_person_discount = discount / len(people)
        for person in people:
            totals[person] -= per_person_discount

    displayed = {person: round(amount, 2) for person, amount in totals.items()}
    grand_total = round(sum(float(item.get("price", 0)) for item in items) * (1 + tax_rate + tip_rate) - discount, 2)

    return {
        "people": displayed,
        "grand_total": grand_total,
    }