"""Workshop 2 Part D solution: pytest tests for the pipeline functions."""
import pytest

from models import Transaction
from transforms import clean_names, remove_invalid


def test_clean_names():
    rows = [{"product_name": "  laptop PRO ", "price": "999.99", "quantity": "2"}]
    result = clean_names(rows)
    assert result[0]["product_name"] == "Laptop Pro"
    assert rows[0]["product_name"] == "  laptop PRO "  # original unchanged


def test_remove_invalid():
    rows = [
        {"product_name": "Laptop", "price": "-10", "quantity": "1"},
        {"product_name": "Mouse", "price": "29.99", "quantity": "0"},
        {"product_name": "Keyboard", "price": "89.99", "quantity": "2"},
    ]
    result = remove_invalid(rows)
    assert len(result) == 1
    assert result[0]["product_name"] == "Keyboard"


def test_transaction_rejects_bad_row():
    with pytest.raises(ValueError):
        Transaction(product_name="", price=10.0, quantity=1, revenue=10.0)
    with pytest.raises(ValueError):
        Transaction(product_name="Mouse", price=-5.0, quantity=1, revenue=0.0)
