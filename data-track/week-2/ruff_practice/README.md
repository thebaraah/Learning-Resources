# Ruff Practice (Week 2 Ch8)

A deliberately messy Python file plus a tiny `pyproject.toml` so ruff has the right rule sets enabled. Goal: run `ruff check`, identify each rule code, fix them one at a time, re-run.

## Setup

```bash
pip install ruff
mkdir -p ruff_practice && cd ruff_practice
curl -L https://gist.githubusercontent.com/lassebenni/38c2e8fb384302cdcd2d0ecc82120b16/raw/messy.py -o messy.py
curl -L https://gist.githubusercontent.com/lassebenni/38c2e8fb384302cdcd2d0ecc82120b16/raw/pyproject.toml -o pyproject.toml
ruff check messy.py
```

You should see **6 errors across 5 distinct rule codes**: F401 (twice, two unused imports), F841, B006, E501, E711. Fix them one at a time and re-run.

> 💡 The local `pyproject.toml` enables the `B` (bugbear) rule set and pins a line length so all 5 codes light up. Default ruff config would only flag 3 of them.

When stuck, compare against `messy_fixed.py`: but only after attempting.
