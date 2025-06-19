import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def db():
    return Database()


def test_available_buns(db):
    buns = db.available_buns()
    assert len(buns) == 3

    expected = [("black bun", 100), ("white bun", 200), ("red bun", 300)]
    actual = [(bun.get_name(), bun.get_price()) for bun in buns]
    assert actual == expected


def test_available_ingredients(db):
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6

    sauces = ingredients[:3]
    fillings = ingredients[3:]

    expected_sauces = [("hot sauce", 100), ("sour cream", 200), ("chili sauce", 300)]
    expected_fillings = [("cutlet", 100), ("dinosaur", 200), ("sausage", 300)]

    actual_sauces = [(i.get_name(), i.get_price()) for i in sauces if i.get_type() == INGREDIENT_TYPE_SAUCE]
    actual_fillings = [(i.get_name(), i.get_price()) for i in fillings if i.get_type() == INGREDIENT_TYPE_FILLING]

    assert actual_sauces == expected_sauces
    assert actual_fillings == expected_fillings
