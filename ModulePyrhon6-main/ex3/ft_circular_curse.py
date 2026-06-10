from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients

if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredient validation:")
    print("validate_ingredients('fire air'):", end=" ")
    print(validate_ingredients("fire"))
    print("validate_ingredients('dragon scales'):", end=" ")
    print(validate_ingredients("dragon scales"))
    print()
    print("Testing spell recording with validation:")
    print("record_spell('Fireball', 'fire air'):", end=" ")
    print(record_spell("Fireball", "fire air"))
    print()
    print("Testing late import technique:")
    print("record_spell('Lightning', 'air'):", end=" ")
    print(record_spell("Lightning", "air"))
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
