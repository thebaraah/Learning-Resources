"""Workshop 1 Part B starter.

You start with the disaster loop inlined. Refactor in three steps:

  1. Replace the hardcoded path with `from config import INPUT_PATH, OUTPUT_PATH`.
  2. Extract `clean_names(rows)`: strips + title-cases product_name. Return a NEW list.
  3. Extract `calculate_revenue(rows)`: adds revenue + vat fields. Return a NEW list.
  4. Chain: data = clean_names(raw); data = calculate_revenue(data).
  5. Print raw[0] after the chain. It should be unchanged.

Hint: use {**row, "key": val} to copy-with-update without mutating the input row.
"""

import csv


def load_rows(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(path: str, rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)


# TODO: clean_names(rows) -> list[dict]
# TODO: calculate_revenue(rows) -> list[dict]


if __name__ == "__main__":
    raw = load_rows("data/sales.csv")  # TODO: use INPUT_PATH from config
    # TODO: chain the transforms
    data = raw
    print("raw[0] after pipeline:", raw[0])  # should match the file, unchanged
    write_rows("output/clean.csv", data)  # TODO: use OUTPUT_PATH from config
