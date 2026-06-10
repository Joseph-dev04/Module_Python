from typing import Callable


#Combina dos spells
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (
        spell1(target, power),
        spell2(target, power),
    )


#Amplifica el poder
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


#Ejecuta condicionalmente
def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power)
        if condition(target, power)
        else "Spell fizzled"
    )


#Secuencia de spells
def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [
        spell(target, power) for spell in spells
    ]


#spells base
def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


#condición ejemplo
def strong_enough(target: str, power: int) -> bool:
    return power >= 20


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Orc", 10))
    print("Amplified:", mega_fireball("Orc", 10))

    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(strong_enough, fireball)
    print(conditional_spell("Goblin", 10))   # fizzled
    print(conditional_spell("Goblin", 25))   # works

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, lightning])
    results = combo("Troll", 15)
    for r in results:
        print(r)


if __name__ == "__main__":
    main()