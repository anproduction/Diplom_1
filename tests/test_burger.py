import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_price.return_value = 100.0
    bun.get_name.return_value = "Классическая булочка"
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 50.0
    ingredient.get_name.return_value = "Соус фирменный"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient


def test_set_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients


def test_remove_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    ingredient2 = MagicMock()
    ingredient2.get_price.return_value = 30.0
    ingredient2.get_name.return_value = "Салат"
    ingredient2.get_type.return_value = "FILLING"
    burger.add_ingredient(ingredient2)

    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == mock_ingredient


def test_get_price(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(mock_ingredient)  # два одинаковых ингредиента
    expected_price = 100.0 * 2 + 50.0 * 2
    assert burger.get_price() == expected_price


def test_get_receipt(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    receipt = burger.get_receipt()

    assert "(==== Классическая булочка ====)" in receipt
    assert "= sauce Соус фирменный =" in receipt
    assert "Price: 250.0" in receipt
