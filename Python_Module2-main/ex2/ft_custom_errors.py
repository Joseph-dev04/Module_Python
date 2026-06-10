class GardenErrors(Exception):
    pass


class PlantErrors(GardenErrors):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__message = f"The {name} plant is wilting!"
        super().__init__(self.__message)


class WaterErrors(GardenErrors):
    def __init__(self, amount: int) -> None:
        self.__amount = amount
        self.__message = f"Not enough water in the tank! : {amount}"
        super().__init__(self.__message)


def test_plant() -> None:
    raise PlantErrors("tomato")


def test_water() -> None:
    raise WaterErrors(0)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        test_plant()
    except PlantErrors as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        test_water()
    except WaterErrors as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        test_plant()
    except PlantErrors as e:
        print(f"Caught PlantError: {e}")
    try:
        test_water()
    except WaterErrors as e:
        print(f"Caught WaterError: {e}")
    print("All custom error types work correctly!")
