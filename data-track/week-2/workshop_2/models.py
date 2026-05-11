"""Workshop 2 Part B starter: define the Transaction dataclass.

Note: @dataclass is a decorator — Python's shorthand for applying the
dataclass() function to a class to auto-generate __init__, __repr__, and more.
You'll see @dataclass above the class definition in the solution.

TODO:
  1. Import dataclass from the dataclasses module and add @dataclass to the class.
  2. Fields: product_name (str), price (float), quantity (int), revenue (float).
  3. Add __post_init__ validation that raises ValueError when:
       - price < 0
       - product_name is empty after strip()
  4. Try Transaction(product_name="", price=-5, quantity=1, revenue=0).
     It should crash here, not in next Monday's CEO report.
"""


class Transaction:
    pass
