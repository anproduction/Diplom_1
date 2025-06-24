from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import EXPECTED_BUNS, EXPECTED_SAUCES, EXPECTED_FILLINGS


class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == len(EXPECTED_BUNS)

        actual = [(bun.get_name(), bun.get_price()) for bun in buns]
        assert actual == EXPECTED_BUNS

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == len(EXPECTED_SAUCES) + len(EXPECTED_FILLINGS)

        sauces = ingredients[:len(EXPECTED_SAUCES)]
        fillings = ingredients[len(EXPECTED_SAUCES):]

        actual_sauces = [(i.get_name(), i.get_price()) for i in sauces if i.get_type() == INGREDIENT_TYPE_SAUCE]
        actual_fillings = [(i.get_name(), i.get_price()) for i in fillings if i.get_type() == INGREDIENT_TYPE_FILLING]

        assert actual_sauces == EXPECTED_SAUCES
        assert actual_fillings == EXPECTED_FILLINGS
