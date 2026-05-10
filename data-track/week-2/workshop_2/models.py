"""Workshop 2 Part B starter: define the Transaction dataclass.

TODO:
  1. Make this a @dataclass.
  2. Fields: product_name (str), price (float), quantity (int), revenue (float).
  3. Add __post_init__ validation that raises ValueError when:
       - price < 0
       - product_name is empty after strip()
  4. Try Transaction(product_name="", price=-5, quantity=1, revenue=0).
     It should crash here, not in next Monday's CEO report.
"""


class Transaction:
    pass
