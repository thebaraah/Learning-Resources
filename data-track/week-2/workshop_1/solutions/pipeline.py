"""Workshop 1 Part B solution: pure transforms, no mutation.

The {**row, "key": val} pattern is the whole point: each transform copies the row,
adds or rewrites the named field, and returns a NEW list. The caller's `raw` is
untouched, which is what makes the chain testable without a CSV at all.
"""

import csv
from pathlib import Path

from config import INPUT_PATH, OUTPUT_PATH, VAT_RATE


def load_rows(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(path: str, rows: list[dict]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)


def clean_names(rows: list[dict]) -> list[dict]:
    return [{**r, "product_name": r["product_name"].strip().title()} for r in rows]


def calculate_revenue(rows: list[dict]) -> list[dict]:
    out = []
    for r in rows:
        revenue = float(r["price"]) * int(r["quantity"])
        out.append({**r, "revenue": revenue, "vat": revenue * VAT_RATE})
    return out


if __name__ == "__main__":
    raw = load_rows(INPUT_PATH)
    data = clean_names(raw)
    data = calculate_revenue(data)

    # Proof of no mutation: raw[0] should still match what's on disk.
    print("raw[0] after pipeline:", raw[0])
    print("data[0] after pipeline:", data[0])

    write_rows(OUTPUT_PATH, data)
    print(f"Wrote {len(data)} rows to {OUTPUT_PATH}")
