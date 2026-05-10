"""Workshop 2 Part C starter: composable transforms, no mutation.

TODO:
  1. clean_names(rows): strip + title-case product_name.
  2. calculate_revenue(rows): add revenue + vat.
  3. remove_invalid(rows): drop rows where price <= 0 or quantity <= 0.

Each function returns a NEW list. Use {**row, "key": val} to copy.
"""


def clean_names(rows: list[dict]) -> list[dict]:
    raise NotImplementedError


def calculate_revenue(rows: list[dict]) -> list[dict]:
    raise NotImplementedError


def remove_invalid(rows: list[dict]) -> list[dict]:
    raise NotImplementedError
