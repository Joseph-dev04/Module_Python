def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    col = light_spell_allowed_ingredients()
    if any(i in ingredients for i in col):
        return f"({ingredients} - VALID)"
    else:
        return f"({ingredients} - INVALID)"