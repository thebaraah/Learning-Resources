"""Exercise 3: Separate I/O from Logic.

The god function below reads a CSV, computes total revenue, and writes
a report file all in one go. Split it into:

  - read_sales(path) -> list[dict]            (I/O)
  - calculate_revenue(rows) -> float          (pure logic, NO file access)
  - write_report(total, path) -> None         (I/O)
  - run_pipeline(input_path, output_path)     (orchestrator)
"""
import csv


# BAD: I/O and logic mixed together
def process_sales():
    with open("sales.csv") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    total = 0.0
    for row in rows:
        price = float(row["price"])
        quantity = int(row["quantity"])
        if price > 0 and quantity > 0:
            total += price * quantity

    with open("report.txt", "w") as f:
        f.write(f"Total revenue: €{total:.2f}")


# TODO 1: read_sales(path) — open the CSV and return list[dict].
#         No filtering, no math, just I/O.
def read_sales(path: str) -> list[dict]:
    raise NotImplementedError


# TODO 2: calculate_revenue(rows) — pure function. Skip rows where
#         price <= 0 or quantity <= 0. Return a float.
def calculate_revenue(rows: list[dict]) -> float:
    raise NotImplementedError


# TODO 3: write_report(total, path) — write the formatted line to disk.
def write_report(total: float, path: str) -> None:
    raise NotImplementedError


# TODO 4: run_pipeline orchestrates the three above in order.
def run_pipeline(input_path: str, output_path: str) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    run_pipeline("sales.csv", "report.txt")
    # Expected report.txt contents (with the provided sales.csv):
    # Total revenue: €125.97
    # (19.99*3 + 49.50*1 + 8.25*2; the 0.00 and -12.00 rows are skipped)
    print("Wrote report.txt")
