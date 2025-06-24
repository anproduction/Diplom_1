import pytest
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from data import INGREDIENT_TEST_DATA


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_ingredient_get_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_ingredient_get_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_ingredient_get_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price


def test_ingredient_types_constants():
    assert ingredient_types.INGREDIENT_TYPE_SAUCE == "SAUCE"
    assert ingredient_types.INGREDIENT_TYPE_FILLING == "FILLING"
