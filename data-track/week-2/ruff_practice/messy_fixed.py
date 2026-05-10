# Reference fix. Compare AFTER you have tried it yourself.
# Each comment marks the rule code that flagged the original line.
# This file passes `ruff check messy_fixed.py` cleanly.

# F401: removed unused `import os`, `import sys`, and `from typing import List`.
# F841: removed the unused `debug_label` local.
# B006: replaced mutable default `cache=[]` with the None sentinel pattern.
# E711: replaced `== None` with `is None`.
# E501: shortened the over-long string.


def process(items: list[str], cache: list[str] | None = None) -> list[str] | None:
    if cache is None:
        cache = []
    if items[0] is None:
        return None
    cache.append(items[0])
    return cache


if __name__ == "__main__":
    print(process(["a", "b"]))
    print(process(["c"]))
