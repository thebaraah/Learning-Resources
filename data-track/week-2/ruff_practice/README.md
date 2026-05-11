# Ruff Practice (Week 2 Ch8)

A deliberately messy Python file plus a tiny `pyproject.toml` so ruff has the right rule sets enabled. Goal: run `ruff check`, identify each rule code, fix them one at a time, re-run.

## Setup

From the Codespace you opened for Week 2 exercises, navigate into this folder:

```bash
cd data-track/week-2/ruff_practice
pip install ruff
ruff check messy.py
```

You should see **6 errors across 5 distinct rule codes**: F401 (twice, two unused imports), F841, B006, E501, E711. Fix them one at a time and re-run.

> 💡 The local `pyproject.toml` enables the `B` (bugbear) rule set and pins a line length so all 5 codes light up. Default ruff config would only flag 3 of them.

When stuck, compare against `messy_fixed.py`: but only after attempting.
