import pytest
from nutrition_calculator import nutritional_summary
@pytest.fixture
def nutrition_data():
    return {
        "Apple": {
            "calories": 52,
            "total_fat": 0.2,
            "protein": 0.3,
            "carbohydrate": 14,
            "sugars": 10
        }
    }
def test_valid_food_returns_summary(nutrition_data):
    result = nutritional_summary(
        {"Apple": 100},
        nutrition_data
    )
    assert result["calories"] == 52
def test_unknown_food_raises_error(nutrition_data):
    with pytest.raises(ValueError):
        nutritional_summary(
            {"Banana": 100},
            nutrition_data
        )
def test_negative_weight_raises_error(nutrition_data):
    with pytest.raises(ValueError):
        nutritional_summary(
            {"Apple": -100},
            nutrition_data
        )
def test_zero_weight_raises_error(nutrition_data):
    with pytest.raises(ValueError):
        nutritional_summary(
            {"Apple": 0},
            nutrition_data
        )
def test_text_weight_raises_error(nutrition_data):
    with pytest.raises(TypeError):
        nutritional_summary(
            {"Apple": "one hundred"},
            nutrition_data
        )
def test_empty_food_dictionary_raises_error(nutrition_data):
    with pytest.raises(ValueError):
        nutritional_summary(
            {},
            nutrition_data
        )
