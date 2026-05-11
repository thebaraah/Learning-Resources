"""Workshop 2 Part C solution: chain transforms, count at each step.

Reorder discussion: if calculate_revenue runs BEFORE remove_invalid, negative-price
rows get included in the revenue total. Order is part of the contract.
"""

import csv
from pathlib import Path

from models import Transaction
from transforms import calculate_revenue, clean_names, remove_invalid

_ROOT = Path(__file__).resolve().parent.parent  # workshop_2/


def load_rows(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    raw = load_rows(_ROOT / "data" / "sales.csv")
    print(f"raw: {len(raw)} rows")

    data = remove_invalid(raw)
    print(f"after remove_invalid: {len(data)} rows")

    data = clean_names(data)
    print(f"after clean_names: {len(data)} rows")

    data = calculate_revenue(data)
    print(f"after calculate_revenue: {len(data)} rows")

    transactions: list[Transaction] = []
    for r in data:
        try:
            transactions.append(
                Transaction(
                    product_name=r["product_name"],
                    price=float(r["price"]),
                    quantity=int(r["quantity"]),
                    revenue=r["revenue"],
                )
            )
        except ValueError as e:
            print(f"  skipped row {r.get('transaction_id')}: {e}")

    print(f"
final: {len(transactions)} valid Transactions")
    print(f"total revenue: {sum(t.revenue for t in transactions):.2f}")

    (_ROOT / "output").mkdir(exist_ok=True)
