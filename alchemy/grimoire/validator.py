def validate_ingredients(ingredients: str) -> str:
    ingredients_new = ingredients.split()
    valid_data = ["fire", "water", "earth", "air"]

    for ingredient in ingredients_new:
        if ingredient not in valid_data:
            return f"{ingredients} INVALID"
    return f"{ingredients} VALID"
