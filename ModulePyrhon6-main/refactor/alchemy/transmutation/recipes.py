from alchemy import create_air, strength_potion
import elements

def lead_to_gold() -> str:
    message = "Recipe transmuting Lead to Gold: brew '"
    message += create_air()
    message += f"' and '{strength_potion()}' mixed with '{elements.create_fire()}'"
    return message
