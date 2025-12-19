import pytest

@pytest.mark.parametrize("price, expected", [
    (100, 100),
    (200, 200),
    (500, 500)
])
def test_price_logic(price, expected):
    # Egyszerű funkcionális teszt példa [cite: 17]
    assert price == expected