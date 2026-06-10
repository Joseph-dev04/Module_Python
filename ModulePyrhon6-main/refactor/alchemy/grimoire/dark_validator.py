from .dark_spellbook import dark_spell_allowed_ingredients
def validate_ingredients1(ingredients: str) -> str:
    col = dark_spell_allowed_ingredients()
    if all(i in ingredients for i in col):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"