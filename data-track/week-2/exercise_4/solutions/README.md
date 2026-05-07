# Week 2 — Exercise 4: Write Tests with Pytest

**Concepts:** `pytest`, `assert`, `@pytest.fixture`, `@pytest.mark.parametrize`.

## Setup

```bash
pip install -r requirements.txt
```

The function under test is `calculate_revenue` in `sales.py` (a reference copy that matches Exercise 3's contract). You are **not** modifying `sales.py` — you are writing the tests against it.

## Your task

Fill in the four test placeholders in `test_sales.py`:

1. **`test_calculate_revenue_basic`** — pass two valid rows, assert the right total.
2. **`test_calculate_revenue_skips_invalid`** — pass rows with `price <= 0` and `quantity <= 0`, assert they're excluded.
3. **A `sample_rows` fixture** — a `@pytest.fixture` that returns a reusable list of dicts. Use it in at least one test.
4. **A parametrized test** — `@pytest.mark.parametrize` covering at least: empty list, one valid row, one zero-price row.

Run:

```bash
pytest test_sales.py -v
```

## Success criteria

All tests pass. Each test is independent (no test depends on another's side effects). Pytest reports each parametrized case as a separately-named test in the output.

## Stretch

Add a test that uses `pytest.approx()` to compare a float total — useful when `price * rate` produces fractional results that don't match `==` exactly.
