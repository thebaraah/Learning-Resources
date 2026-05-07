"""Reference solution (in-place over the starter)."""
import pytest
from sales import calculate_revenue


# TODO 1: test_calculate_revenue_basic
# Pass two valid rows (e.g. price 10/qty 2, price 5/qty 3). Assert the
# returned total is 35.0.
# WHY one assertion per test: when this fails, pytest's output points
# at the exact line. A test with five asserts hides which one broke.
def test_calculate_revenue_basic():
    rows = [
        {"price": "10", "quantity": "2"},
        {"price": "5", "quantity": "3"},
    ]
    assert calculate_revenue(rows) == 35.0


# TODO 2: test_calculate_revenue_skips_invalid
# Pass rows that should be skipped: price=0, price negative, quantity=0,
# quantity negative. Assert the total is 0.0 (or matches only the valid
# rows you also pass in).
# WHY mix valid + invalid in one test: proves the function correctly
# *partitions* rows. Asserting "5 invalid rows -> 0.0" only proves the
# function returns 0 for empty input; mixing in one valid row makes
# sure the filter works alongside the math.
def test_calculate_revenue_skips_invalid():
    rows = [
        {"price": "10", "quantity": "2"},   # valid -> 20.0
        {"price": "0", "quantity": "5"},    # zero price -> skipped
        {"price": "-5", "quantity": "3"},   # negative price -> skipped
        {"price": "8", "quantity": "0"},    # zero quantity -> skipped
        {"price": "8", "quantity": "-1"},   # negative quantity -> skipped
    ]
    assert calculate_revenue(rows) == 20.0


# TODO 3: A pytest fixture called `sample_rows` that returns a small
# reusable list of dicts. Then a test that uses it.
# WHY a fixture: tests that share setup data otherwise repeat the
# same list literal. The fixture is the single source of truth — change
# the data in one place and every test using it updates.
@pytest.fixture
def sample_rows() -> list[dict]:
    return [
        {"price": "20", "quantity": "1"},
        {"price": "5", "quantity": "4"},
    ]


def test_calculate_revenue_with_fixture(sample_rows):
    # WHY the fixture parameter has the same name as the @fixture
    # function: pytest matches them by name. The function above is
    # called and its return value is injected.
    assert calculate_revenue(sample_rows) == 40.0


# TODO 4: A parametrized test using @pytest.mark.parametrize. Cover at
# least: empty list -> 0.0, single valid row -> price*qty, single zero-
# price row -> 0.0.
# WHY parametrize beats a for-loop: each (rows, expected) pair becomes
# a separately-named test in pytest's output. If the zero-price case
# fails, you see "test_calculate_revenue[case2]" — not "1 of 4 asserts
# in test_calculate_revenue failed".
@pytest.mark.parametrize(
    "rows, expected",
    [
        ([], 0.0),                                          # empty list
        ([{"price": "12", "quantity": "3"}], 36.0),         # single valid
        ([{"price": "0", "quantity": "5"}], 0.0),           # single zero-price
        ([{"price": "5", "quantity": "0"}], 0.0),           # single zero-quantity
    ],
)
def test_calculate_revenue_edge_cases(rows, expected):
    assert calculate_revenue(rows) == expected


# Run with: pytest test_sales.py -v
