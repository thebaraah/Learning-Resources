"""Exercise 4: Write Tests with Pytest.

The `calculate_revenue` function is in `sales.py`. Write tests that
prove it does what its docstring promises.
"""
import pytest
from sales import calculate_revenue


# TODO 1: test_calculate_revenue_basic
# Pass two valid rows (e.g. price 10/qty 2, price 5/qty 3). Assert the
# returned total is 35.0.
def test_calculate_revenue_basic():
    raise NotImplementedError


# TODO 2: test_calculate_revenue_skips_invalid
# Pass rows that should be skipped: price=0, price negative, quantity=0,
# quantity negative. Assert the total is 0.0 (or matches only the valid
# rows you also pass in).
def test_calculate_revenue_skips_invalid():
    raise NotImplementedError


# TODO 3: A pytest fixture called `sample_rows` that returns a small
# reusable list of dicts. Then a test that uses it.
# Hint: decorate a function with @pytest.fixture and have it return a list.


# TODO 4: A parametrized test using @pytest.mark.parametrize. Cover at
# least: empty list -> 0.0, single valid row -> price*qty, single zero-
# price row -> 0.0.


# Run with: pytest test_sales.py -v
