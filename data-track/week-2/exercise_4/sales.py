"""A reference `calculate_revenue` matching Exercise 3's contract.

Exercise 4 is about TESTING this function — not implementing it. If you
want to test your own Exercise 3 solution, copy that file's
`calculate_revenue` into here.
"""


def calculate_revenue(rows: list[dict]) -> float:
    """Sum price * quantity, skipping rows with price <= 0 or quantity <= 0."""
    total = 0.0
    for row in rows:
        price = float(row["price"])
        quantity = int(row["quantity"])
        if price > 0 and quantity > 0:
            total += price * quantity
    return total
