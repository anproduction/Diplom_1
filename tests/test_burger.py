from unittest.mock import MagicMock
from praktikum.burger import Burger
from data import (
    SECOND_INGREDIENT_NAME, SECOND_INGREDIENT_PRICE, SECOND_INGREDIENT_TYPE,
)

class TestBurger:

    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        ingredient2 = MagicMock()
        ingredient2.get_price.return_value = SECOND_INGREDIENT_PRICE
        ingredient2.get_name.return_value = SECOND_INGREDIENT_NAME
        ingredient2.get_type.return_value = SECOND_INGREDIENT_TYPE

        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == mock_ingredient

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        expected_price = mock_bun.get_price.return_value * 2 + mock_ingredient.get_price.return_value * 2
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        expected_receipt = (
            f"(==== {mock_bun.get_name.return_value} ====)\n"
            f"= {mock_ingredient.get_type.return_value.lower()} {mock_ingredient.get_name.return_value} =\n"
            f"(==== {mock_bun.get_name.return_value} ====)\n"
            f"Price: {mock_bun.get_price.return_value * 2 + mock_ingredient.get_price.return_value}"
        )

        assert receipt == expected_receipt
