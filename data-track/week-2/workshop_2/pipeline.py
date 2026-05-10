"""Workshop 2 Part C starter: wire it all together.

TODO:
  1. Chain: remove_invalid -> clean_names -> calculate_revenue.
  2. Print the row count after EACH step. Watch the data shrink.
  3. Convert each cleaned dict to a Transaction (you'll catch any bad rows here).
  4. Discussion: what breaks if calculate_revenue runs BEFORE remove_invalid?

(Loading config from .env was Workshop 1's job; here we hardcode the path
to keep focus on the dataclass + composition pieces.)
"""

import csv

from models import Transaction  # noqa: F401
from transforms import calculate_revenue, clean_names, remove_invalid  # noqa: F401


def load_rows(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    raw = load_rows("data/sales.csv")
    print(f"raw: {len(raw)} rows")
    # TODO: chain the three transforms, printing the count at each step.
    # TODO: convert each final row to a Transaction. Crash on bad rows is OK.
