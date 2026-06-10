from typing import Callable


#contador con closure
def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


#acumulador de poder
def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulate(amount: int):
        nonlocal total
        total += amount
        return total

    return accumulate


#factory de encantamientos
def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"

    return enchant


#sistema de memoria
def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: str, value):
        storage[key] = value

    def recall(key: str):
        return storage.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


#demo
def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print("Base 100, add 20:", acc(20))
    print("Base 100, add 30:", acc(30))

    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")

    print(fire("Sword"))
    print(ice("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["store"]("secret", 42)
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()