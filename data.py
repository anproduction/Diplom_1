# Булочки для параметризации
BUN_TEST_DATA = [
    ("Классическая булочка", 100.0),
    ("Булочка с кунжутом", 120.5),
    ("Черная булочка", 130.75),
]

# Ожидаемые булочки
EXPECTED_BUNS = [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
]

# Ожидаемые соусы и начинки
EXPECTED_SAUCES = [
    ("hot sauce", 100),
    ("sour cream", 200),
    ("chili sauce", 300),
]

EXPECTED_FILLINGS = [
    ("cutlet", 100),
    ("dinosaur", 200),
    ("sausage", 300),
]

# Данные для мок-булочки
MOCK_BUN_NAME = "Классическая булочка"
MOCK_BUN_PRICE = 100.0

# Данные для мок-ингредиента
MOCK_INGREDIENT_NAME = "Соус фирменный"
MOCK_INGREDIENT_TYPE = "SAUCE"
MOCK_INGREDIENT_PRICE = 50.0

# Второй ингредиент для теста перемещения
SECOND_INGREDIENT_NAME = "Салат"
SECOND_INGREDIENT_TYPE = "FILLING"
SECOND_INGREDIENT_PRICE = 30.0

# Ингредиенты для параметризации
INGREDIENT_TEST_DATA = [
    ("SAUCE", "Барбекю", 50.0),
    ("FILLING", "Котлета", 150.0),
    ("UNKNOWN", "Что-то странное", 0.0),
]
