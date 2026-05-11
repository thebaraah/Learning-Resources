"""Workshop 2 Part D starter: test your pipeline functions.

TODO: write three pytest tests.

  1. test_clean_names: assert product names are stripped and title-cased.
     Bonus: assert the original input row is unchanged (no mutation).
  2. test_remove_invalid: assert rows with price <= 0 or quantity <= 0 are dropped.
  3. test_transaction_rejects_bad_row: assert ValueError is raised for an empty
     product_name and for a negative price.

Run with: pytest test_pipeline.py -v
"""
import pytest

from models import Transaction
from transforms import clean_names, remove_invalid


def test_clean_names():
    # TODO: build a one-row input with a messy product_name.
    # Assert the output is stripped and title-cased.
    # Assert the original input row is unchanged.
    pass


def test_remove_invalid():
    # TODO: build rows with negative price and zero quantity.
    # Assert only the valid row survives.
    pass


def test_transaction_rejects_bad_row():
    # TODO: use pytest.raises(ValueError) to assert that Transaction rejects
    # an empty product_name and a negative price.
    pass
