# A deliberately messy file. From this folder, run `ruff check messy.py`
# (the local pyproject.toml enables the rule sets you need).
# Fix violations one by one. Re-run after each fix to watch the count drop.
#
# Rule codes you should see (do not peek at the names until after you run ruff):
# F401, F841, B006, E501, E711

import os
import sys
from typing import List


def process(items: List[str], cache=[]):
    if items[0] == None:
        return None
    cache.append(items[0])
    summary = "result-summary-prefix-that-pushes-this-line-well-past-the-default-line-length"
    return cache


if __name__ == "__main__":
    print(process(["a", "b"]))
    print(process(["c"]))
