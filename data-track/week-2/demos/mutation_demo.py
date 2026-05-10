"""Gotcha #1 demo: in-place mutation corrupts the caller's data.

Run: python mutation_demo.py
"""


def apply_vat_bad(rows: list[dict]) -> list[dict]:
    """Looks correct. Tests pass. Silently corrupts the input."""
    for r in rows:
        r["price"] *= 1.21
    return rows


def apply_vat_good(rows: list[dict]) -> list[dict]:
    """The fix: copy-with-update returns a new list, leaves the input untouched."""
    return [{**r, "price": r["price"] * 1.21} for r in rows]


if __name__ == "__main__":
    raw = [{"name": "laptop", "price": 1000.0}]

    print("BAD:")
    print(f"  before: raw[0] = {raw[0]}")
    apply_vat_bad(raw)
    print(f"  after : raw[0] = {raw[0]}  <-- raw was mutated!")

    raw = [{"name": "laptop", "price": 1000.0}]
    print("\nGOOD:")
    print(f"  before: raw[0] = {raw[0]}")
    apply_vat_good(raw)
    print(f"  after : raw[0] = {raw[0]}  <-- raw is untouched")
