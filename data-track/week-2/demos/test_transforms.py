"""Live-coded testing demo (slide §7).

The whole point: no CSV file is needed. Pure functions take inputs and return
outputs, so the tests are explicit and fast.

Run: pytest -v test_transforms.py
"""

from transforms import calculate_revenue, clean_names


def test_clean_names_strips_whitespace():
    data = [{"product_name": "  LAPTOP  ", "price": 999}]
    assert clean_names(data)[0]["product_name"] == "Laptop"


def test_clean_names_does_not_mutate():
    data = [{"product_name": "  mouse  ", "price": 25}]
    clean_names(data)
    assert data[0]["product_name"] == "  mouse  "


def test_calculate_revenue():
    data = [{"product_name": "Widget", "price": 100, "quantity": 3}]
    result = calculate_revenue(data)
    assert result[0]["revenue"] == 300
