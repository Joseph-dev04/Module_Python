from .elements import create_air, create_earth, create_fire, create_water


def healing_potion() -> None:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> None:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> None:
    data = "Invisibility potion brewed with"
    return f"{data} {create_air()} and {create_water()}"


def wisdom_potion() -> None:
    data = "Wisdom poriton brewed with all elements:"
    return f"{data} {create_air} {create_earth} {create_fire} {create_water}"
