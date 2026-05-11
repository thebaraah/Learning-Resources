"""Exercise 6 — Reference solution: OOP vs Functional.

Decision for each snippet and the refactored versions.
"""

# ---------------------------------------------------------------------------
# Snippet A — REFACTOR TO FUNCTION
# WHY: NameCleaner holds no state in self. __init__ is never defined;
# the class is just a wrapper around a single method. Every call to .clean()
# takes rows in and returns rows out, with nothing stored between calls.
# A class with no state is ceremony: it adds a constructor and dot-access
# without buying testability or reuse. The plain function is shorter,
# directly callable, and composable with other transforms.
# ---------------------------------------------------------------------------

def clean_names(rows: list[dict]) -> list[dict]:
    return [
        {**r, "product_name": r["product_name"].strip().title()}
        for r in rows
    ]


# ---------------------------------------------------------------------------
# Snippet B — KEEP AS CLASS
# WHY: DatabaseSink holds two pieces of shared state: self._written
# (the accumulated rows, which grows across calls to .write()) and
# self.written_count (a counter that persists across calls). Both are
# threaded through multiple methods via self. You cannot convert this to
# a plain function without either returning mutable state from every call
# (awkward) or using a global (fragile). When state accumulates across
# calls and must be shared by multiple methods, a class earns its place.
# ---------------------------------------------------------------------------

class DatabaseSink:
    def __init__(self):
        self._written: list[dict] = []
        self.written_count: int = 0

    def write(self, row: dict) -> None:
        self._written.append(row)
        self.written_count += 1

    def flush(self) -> list[dict]:
        return self._written


# ---------------------------------------------------------------------------
# Snippet C — REFACTOR TO FUNCTION
# WHY: ReportFormatter is the same pattern as Snippet A. No self state,
# no __init__, one method that takes rows in and returns a string out.
# The class adds nothing; the function is the correct shape.
# ---------------------------------------------------------------------------

def format_report(rows: list[dict]) -> str:
    lines = [
        f"{r['product_name']}: €{float(r['price']):.2f}" for r in rows
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Checks — same as the starter, rewritten to use the refactored functions
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sample_rows = [
        {"product_name": "  widget ", "price": "9.99", "quantity": "3"},
        {"product_name": "gadget",    "price": "24.50", "quantity": "1"},
    ]

    cleaned = clean_names(sample_rows)
    assert cleaned[0]["product_name"] == "Widget"
    print("A:", cleaned)

    sink = DatabaseSink()
    for row in cleaned:
        sink.write(row)
    assert sink.written_count == 2
    print("B: wrote", sink.written_count, "rows")

    report = format_report(cleaned)
    print("C:\n" + report)

    print("\nAll checks passed.")
