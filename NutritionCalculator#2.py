import json
# Load the nutrition data from a JSON file
def load_nutrition_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"The nutrition file '{file_path}' could not be found."
        )
    except json.JSONDecodeError:
        raise ValueError(
            f"The nutrition file '{file_path}' contains invalid JSON."
        )
# Calculate the nutritional totals for the supplied foods
def nutritional_summary(foods, nutrition_dict):
    # Check that foods have been supplied as a dictionary
    if not isinstance(foods, dict):
        raise TypeError(
            "Foods must be provided as a dictionary."
        )
    # Check that the food dictionary is not empty
    if not foods:
        raise ValueError(
            "At least one food must be provided."
        )
    # Store the total nutritional values
    result_dict = {
        "calories": 0,
        "total_fat": 0,
        "protein": 0,
        "carbohydrate": 0,
        "sugars": 0
    }
    # Process each food item and its weight
    for name, grams in foods.items():
        # Check whether the food exists
        if name not in nutrition_dict:
            raise ValueError(
                f"The food item '{name}' was not found."
            )
        # Check that the weight is a number
        if not isinstance(grams, (int, float)):
            raise TypeError(
                f"The weight for '{name}' must be a number."
            )
        # Check that the weight is greater than zero
        if grams <= 0:
            raise ValueError(
                f"The weight for '{name}' must be greater than zero."
            )
        # Get the nutritional information for the food
        nutrition = nutrition_dict[name]
        # Calculate each value using the supplied weight
        result_dict["calories"] += (
            grams * nutrition["calories"] / 100
        )
        result_dict["total_fat"] += (
            grams * nutrition["total_fat"] / 100
        )
        result_dict["protein"] += (
            grams * nutrition["protein"] / 100
        )
        result_dict["carbohydrate"] += (
            grams * nutrition["carbohydrate"] / 100
        )
        result_dict["sugars"] += (
            grams * nutrition["sugars"] / 100
        )
    # Round each nutritional total to two decimal places
    for nutrient in result_dict:
        result_dict[nutrient] = round(
            result_dict[nutrient],
            2
        )
    return result_dict
# Run an example calculation
def main():
    try:
        nutrition_dict = load_nutrition_data(
            "nutrition.json"
        )
        foods = {
            "Croissants, cheese": 150,
            "Orange juice, raw": 250
        }
        result = nutritional_summary(
            foods,
            nutrition_dict
        )
        print("Nutritional summary:")
        for nutrient, value in result.items():
            print(f"{nutrient}: {value}")
    except (FileNotFoundError, ValueError, TypeError, KeyError) as error:
        print(f"Error: {error}")
# Only run main when this file is executed directly
if __name__ == "__main__":
    main()
 