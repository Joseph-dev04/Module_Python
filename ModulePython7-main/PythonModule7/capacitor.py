from ex1.folder import TransformCreatureFactory
from ex1.folder import HealingCreatureFactory

def test_healing(factory):
    print("Testing Creature with healing capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

def test_transform(factory):
    print("Testing Creature with transform capability")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main_test():
    test_healing(HealingCreatureFactory())
    test_transform(TransformCreatureFactory())


if __name__ == "__main__":
    main_test()