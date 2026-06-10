import time
from functools import wraps
from typing import Callable


#1. Timer decorator
def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


#2. Power validator (decorator factory)
def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power, *args, **kwargs):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)

        return wrapper

    return decorator


#3. Retry decorator
def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
                    else:
                        return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


#Clase con staticmethod
class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


#funciones de prueba
@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell():
    raise ValueError("Boom!")


def main():
    print("Testing spell timer...")
    result = fireball()
    print("Result:", result)

    print("\nTesting retrying spell...")
    print(unstable_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X1"))

    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()