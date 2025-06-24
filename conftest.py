import pytest
from unittest.mock import MagicMock
from data import (
    MOCK_BUN_NAME, MOCK_BUN_PRICE,
    MOCK_INGREDIENT_NAME, MOCK_INGREDIENT_PRICE, MOCK_INGREDIENT_TYPE,
)


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_price.return_value = MOCK_BUN_PRICE
    bun.get_name.return_value = MOCK_BUN_NAME
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_price.return_value = MOCK_INGREDIENT_PRICE
    ingredient.get_name.return_value = MOCK_INGREDIENT_NAME
    ingredient.get_type.return_value = MOCK_INGREDIENT_TYPE
    return ingredient
