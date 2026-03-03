from . import validator


def record_spell(spell_name: str, ingredients: str) -> str:
    validation_result = validator.validate_ingredients(ingredients)
    if " INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"
    return f"Spell recorded: {spell_name} ({validation_result})"
