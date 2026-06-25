#!/usr/bin/env python3
"""Run deterministic receipt-splitter tests.

Example:
  python3 materials/run_receipt_splitter_tests.py --impl runs/loop/final.py --format markdown
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from decimal import Decimal
from pathlib import Path


TESTS = [
    {
        "id": "T01",
        "rule": "simple equal split",
        "receipt": {
            "people": ["Alice", "Bob"],
            "items": [{"name": "pizza", "price": "10.00", "participants": ["Alice", "Bob"]}],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_people": {"Alice": "5.00", "Bob": "5.00"},
        "expected_total": "10.00",
        "plain": "Two people split one 10.00 item evenly.",
    },
    {
        "id": "T02",
        "rule": "item ownership",
        "receipt": {
            "people": ["Alice", "Bob"],
            "items": [
                {"name": "soup", "price": "12.00", "participants": ["Alice"]},
                {"name": "salad", "price": "8.00", "participants": ["Bob"]},
            ],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_people": {"Alice": "12.00", "Bob": "8.00"},
        "expected_total": "20.00",
        "plain": "Each person pays only for their own item.",
    },
    {
        "id": "T03",
        "rule": "shared subset",
        "receipt": {
            "people": ["Alice", "Bob", "Chen"],
            "items": [{"name": "dessert", "price": "9.00", "participants": ["Alice", "Bob"]}],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_people": {"Alice": "4.50", "Bob": "4.50", "Chen": "0.00"},
        "expected_total": "9.00",
        "plain": "Chen did not eat dessert and owes none of it.",
    },
    {
        "id": "T04",
        "rule": "tax and tip",
        "receipt": {
            "people": ["Alice", "Bob"],
            "items": [
                {"name": "alice entree", "price": "20.00", "participants": ["Alice"]},
                {"name": "bob entree", "price": "30.00", "participants": ["Bob"]},
            ],
            "discount": "0.00",
            "tax_rate": "0.10",
            "tip_rate": "0.20",
        },
        "expected_people": {"Alice": "26.00", "Bob": "39.00"},
        "expected_total": "65.00",
        "plain": "Tax and tip follow each person's subtotal.",
    },
    {
        "id": "T05",
        "rule": "discount before tax/tip",
        "receipt": {
            "people": ["Alice", "Bob"],
            "items": [
                {"name": "alice meal", "price": "30.00", "participants": ["Alice"]},
                {"name": "bob meal", "price": "10.00", "participants": ["Bob"]},
            ],
            "discount": "4.00",
            "tax_rate": "0.10",
            "tip_rate": "0.00",
        },
        "expected_people": {"Alice": "29.70", "Bob": "9.90"},
        "expected_total": "39.60",
        "plain": "The 4.00 discount is applied before tax and allocated proportionally.",
    },
    {
        "id": "T06",
        "rule": "rounding cents",
        "receipt": {
            "people": ["Alice", "Bob", "Chen"],
            "items": [{"name": "noodles", "price": "10.00", "participants": ["Alice", "Bob", "Chen"]}],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_people": {"Alice": "3.34", "Bob": "3.33", "Chen": "3.33"},
        "expected_total": "10.00",
        "plain": "The extra cent goes to Alice because she is first in input order.",
    },
    {
        "id": "T07",
        "rule": "unknown person",
        "receipt": {
            "people": ["Alice", "Bob"],
            "items": [{"name": "tea", "price": "6.00", "participants": ["Dana"]}],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_error": True,
        "plain": "An item cannot charge someone outside the people list.",
    },
    {
        "id": "T08",
        "rule": "empty split list",
        "receipt": {
            "people": ["Alice", "Bob"],
            "items": [{"name": "tea", "price": "6.00", "participants": []}],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_error": True,
        "plain": "Every item needs at least one payer.",
    },
    {
        "id": "T09",
        "rule": "negative price",
        "receipt": {
            "people": ["Alice"],
            "items": [{"name": "bad item", "price": "-1.00", "participants": ["Alice"]}],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_error": True,
        "plain": "Negative item prices are rejected.",
    },
    {
        "id": "T10",
        "rule": "no hidden payer",
        "receipt": {
            "people": ["Alice", "Bob", "Chen"],
            "items": [{"name": "dumplings", "price": "12.00", "participants": ["Alice", "Bob"]}],
            "discount": "0.00",
            "tax_rate": "0.00",
            "tip_rate": "0.00",
        },
        "expected_people": {"Alice": "6.00", "Bob": "6.00", "Chen": "0.00"},
        "expected_total": "12.00",
        "plain": "Chen is on the bill but did not share the item, so Chen owes 0.00.",
    },
    {
        "id": "T11",
        "rule": "invalid rate",
        "receipt": {
            "people": ["Alice"],
            "items": [{"name": "meal", "price": "10.00", "participants": ["Alice"]}],
            "discount": "0.00",
            "tax_rate": "-0.10",
            "tip_rate": "0.00",
        },
        "expected_error": True,
        "plain": "Negative tax or tip rates are rejected.",
    },
]


def load_splitter(path: Path):
    spec = importlib.util.spec_from_file_location("receipt_splitter_impl", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load implementation: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.split_receipt


def cents(value: str) -> int:
    return int((Decimal(value) * 100).to_integral_value())


def normalize_people(result: dict) -> dict[str, str]:
    people = result.get("people", {})
    return {name: f"{Decimal(str(amount)):.2f}" for name, amount in people.items()}


def run_test(split_receipt, test: dict) -> dict:
    try:
        result = split_receipt(test["receipt"])
    except ValueError as exc:
        if test.get("expected_error") and str(exc).strip():
            return {"id": test["id"], "rule": test["rule"], "passed": True, "detail": "clear error", "plain": test["plain"]}
        return {"id": test["id"], "rule": test["rule"], "passed": False, "detail": f"wrong error: {exc}", "plain": test["plain"]}
    except Exception as exc:  # noqa: BLE001
        return {"id": test["id"], "rule": test["rule"], "passed": False, "detail": f"unclear error: {type(exc).__name__}", "plain": test["plain"]}

    if test.get("expected_error"):
        return {"id": test["id"], "rule": test["rule"], "passed": False, "detail": "accepted invalid input", "plain": test["plain"]}

    actual_people = normalize_people(result)
    actual_total = f"{Decimal(str(result.get('grand_total'))):.2f}"
    expected_people = test["expected_people"]
    expected_total = test["expected_total"]
    sum_people = sum(cents(amount) for amount in actual_people.values())
    total_cents = cents(actual_total)

    mismatches = []
    if actual_people != expected_people:
        mismatches.append(f"people {actual_people} != {expected_people}")
    if actual_total != expected_total:
        mismatches.append(f"total {actual_total} != {expected_total}")
    if sum_people != total_cents:
        mismatches.append(f"displayed people sum {sum_people / 100:.2f} != total {actual_total}")

    if mismatches:
        return {"id": test["id"], "rule": test["rule"], "passed": False, "detail": "; ".join(mismatches), "plain": test["plain"]}
    return {"id": test["id"], "rule": test["rule"], "passed": True, "detail": "matches expected", "plain": test["plain"]}


def render_markdown(results: list[dict]) -> str:
    passed = sum(1 for item in results if item["passed"])
    raw_score = passed * 5
    normalized = round(raw_score / 55 * 100, 1)
    lines = [
        f"Passed tests: {passed}/11",
        f"Raw score: {raw_score}/55",
        f"Normalized score: {normalized:.1f}/100",
        "",
        "| Test | Rule being checked | Result | Plain-English result |",
        "|---|---|---|---|",
    ]
    for item in results:
        result = "PASS" if item["passed"] else f"FAIL — {item['detail']}"
        lines.append(f"| {item['id']} | {item['rule']} | {result} | {item['plain']} |")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--impl", required=True, type=Path)
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    split_receipt = load_splitter(args.impl)
    results = [run_test(split_receipt, test) for test in TESTS]
    passed = sum(1 for item in results if item["passed"])
    payload = {
        "passed": passed,
        "total": len(TESTS),
        "raw_score": passed * 5,
        "max_raw_score": 55,
        "normalized_score_100": round((passed * 5) / 55 * 100, 1),
        "results": results,
    }
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())