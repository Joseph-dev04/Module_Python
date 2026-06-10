from .dark_validator import validate_ingredients1
def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return f"{spell_name} {validate_ingredients1(ingredients)}"