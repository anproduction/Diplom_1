import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("Классическая булочка", 100.0),
    ("Булочка с кунжутом", 120.5),
    ("Черная булочка", 130.75),
])
def test_bun_initialization_and_getters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
