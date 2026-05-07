"""Reference solution (in-place over the starter)."""
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
# WHY just I/O: this function answers exactly one question: "how do I
# get the data in?". It does not decide what's valid or what's a row
# worth keeping. That decision belongs in calculate_revenue.
def read_sales(path: str) -> list[dict]:
    with open(path) as f:
        return list(csv.DictReader(f))


# TODO 2: calculate_revenue(rows) — pure function. Skip rows where
#         price <= 0 or quantity <= 0. Return a float.
# WHY pure: takes data in, returns data out, no file system, no globals.
# That means we can write `calculate_revenue([{"price": "10", "quantity":
# "2"}])` in a test and get 20.0 — no fixture files, no setup. The whole
# point of the I/O-vs-logic split is that this line works.
def calculate_revenue(rows: list[dict]) -> float:
    total = 0.0
    for row in rows:
        price = float(row["price"])
        quantity = int(row["quantity"])
        if price > 0 and quantity > 0:
            total += price * quantity
    return total


# TODO 3: write_report(total, path) — write the formatted line to disk.
def write_report(total: float, path: str) -> None:
    with open(path, "w") as f:
        f.write(f"Total revenue: €{total:.2f}")


# TODO 4: run_pipeline orchestrates the three above in order.
# WHY a separate orchestrator: the orchestrator is the *only* function
# that knows about both I/O and logic. Each individual function above
# stays single-purpose. If we later need to swap the CSV source for an
# API, only run_pipeline + the new I/O function change.
def run_pipeline(input_path: str, output_path: str) -> None:
    rows = read_sales(input_path)
    total = calculate_revenue(rows)
    write_report(total, output_path)


if __name__ == "__main__":
    run_pipeline("sales.csv", "report.txt")
    # Expected report.txt contents (with the provided sales.csv):
    # Total revenue: €125.97
    # (19.99*3 + 49.50*1 + 8.25*2; the 0.00 and -12.00 rows are skipped)
    print("Wrote report.txt")
