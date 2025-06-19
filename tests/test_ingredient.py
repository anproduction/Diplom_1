import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum import ingredient_types

@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Барбекю", 50.0),
    (INGREDIENT_TYPE_FILLING, "Котлета", 150.0),
    ("UNKNOWN", "Что-то странное", 0.0),
])
def test_ingredient_initialization_and_getters(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price

def test_ingredient_types_constants():
    assert ingredient_types.INGREDIENT_TYPE_SAUCE == 'SAUCE'
    assert ingredient_types.INGREDIENT_TYPE_FILLING == 'FILLING'
