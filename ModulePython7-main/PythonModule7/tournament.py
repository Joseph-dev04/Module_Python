from ex0 import FlameFactory, AquaFactory
from ex1.folder import HealingCreatureFactory, TransformCreatureFactory
from ex2.Strategy import (
    NormalStrategy,
    AggresiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):

                f1, s1 = opponents[i]
                f2, s2 = opponents[j]

                c1 = f1.create_base()
                c2 = f2.create_base()

                print("* Battle *")
                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")

                s1.act(c1)
                s2.act(c2)

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")

def main():
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggresiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([
        (flame, normal),
        (heal, defensive),
    ])

    print("Tournament 1 (error)")
    battle([
        (flame, aggressive),
        (heal, defensive),
    ])

    print("Tournament 2 (multiple)")
    battle([
        (aqua, normal),
        (heal, defensive),
        (transform, aggressive),
    ])


if __name__ == "__main__":
    main()