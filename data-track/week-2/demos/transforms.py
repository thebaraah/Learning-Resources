"""Pure transforms used by test_transforms.py.

These are the same functions from Workshop 1 Part B, copied here so the test
file can be run standalone without setting up the workshop folder.
"""


def clean_names(rows: list[dict]) -> list[dict]:
    return [{**r, "product_name": r["product_name"].strip().title()} for r in rows]


def calculate_revenue(rows: list[dict]) -> list[dict]:
    out = []
    for r in rows:
        revenue = float(r["price"]) * int(r["quantity"])
        out.append({**r, "revenue": revenue})
    return out
