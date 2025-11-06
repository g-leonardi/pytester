import pytest
from app.app import calculate_discount


@pytest.mark.parametrize("price,discount,expected", [
    (100, 0.2, 80),
    (50, 0.0, 50),
    (75, 1.0, 0)
])
def test_calculate_discount(price, discount, expected):
    assert calculate_discount(price, discount) == expected