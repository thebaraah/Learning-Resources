"""Exercise 6: OOP vs Functional — Spot the State.

Three pipeline components are implemented as classes below.
For each one, decide:
  - KEEP AS CLASS: it holds state that methods share via self
  - REFACTOR TO FUNCTION: it is stateless input -> output

Mark your decision with a comment, then rewrite the ones that
should be functions. The checks at the bottom show you whether
your refactored functions produce the same output.
"""

# ---------------------------------------------------------------------------
# Snippet A
# ---------------------------------------------------------------------------

class NameCleaner:
    """Strips whitespace and title-cases the product_name field of each row."""

    def clean(self, rows: list[dict]) -> list[dict]:
        return [
            {**r, "product_name": r["product_name"].strip().title()}
            for r in rows
        ]


# ---------------------------------------------------------------------------
# Snippet B
# ---------------------------------------------------------------------------

class DatabaseSink:
    """Writes rows to a database and tracks how many were written.

    self._written stubs the DB write (a real version would use a connection
    object like psycopg2.connect(...)). self.written_count persists across
    multiple calls to .write().
    """

    def __init__(self):
        self._written: list[dict] = []   # stands in for a real DB connection
        self.written_count: int = 0

    def write(self, row: dict) -> None:
        self._written.append(row)
        self.written_count += 1

    def flush(self) -> list[dict]:
        return self._written


# ---------------------------------------------------------------------------
# Snippet C
# ---------------------------------------------------------------------------

class ReportFormatter:
    """Formats a list of rows into a human-readable text report."""

    def format(self, rows: list[dict]) -> str:
        lines = [
            f"{r['product_name']}: €{float(r['price']):.2f}" for r in rows
        ]
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Checks — run this file with: python exercise.py
# Once you have refactored, replace the class calls below with your functions.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sample_rows = [
        {"product_name": "  widget ", "price": "9.99", "quantity": "3"},
        {"product_name": "gadget",    "price": "24.50", "quantity": "1"},
    ]

    # Snippet A check
    cleaner = NameCleaner()
    cleaned = cleaner.clean(sample_rows)
    assert cleaned[0]["product_name"] == "Widget", f"Expected 'Widget', got {cleaned[0]['product_name']}"
    print("A:", cleaned)

    # Snippet B check
    sink = DatabaseSink()
    for row in cleaned:
        sink.write(row)
    assert sink.written_count == 2
    print("B: wrote", sink.written_count, "rows")

    # Snippet C check
    formatter = ReportFormatter()
    report = formatter.format(cleaned)
    print("C:\n" + report)

    print("\nAll checks passed.")
