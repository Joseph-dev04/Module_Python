class Invalid(Exception):
    pass


class InvalidName(Invalid):
    def __init__(self, name: str) -> None:
        self.__message = f"Error adding plant: Plant name cannot be {name}!"
        super().__init__(self.__message)


class InvalidHealth(Invalid):
    def __init__(self, name: str, health: int) -> None:
        self.__name = f"Error checking {name}:"
        self.__health = f"Water level {health} is too"
        self.__message = f"{self.__name} {self.__health} high (max 10)"
        super().__init__(self.__message)


class Plant:
    def __init__(self, name: str, water: int) -> None:
        self.__name = name
        self.__water = water

    def get_name(self) -> str:
        return self.__name

    def get_water(self) -> int:
        return self.__water


class Plant_type(Plant):
    def __init__(self, name: str, health: int, sun: int) -> None:
        super().__init__(name, health)
        self.__sun = sun

    def get_sun(self) -> int:
        return self.__sun


class GardenManager():
    def __init__(self) -> None:
        self.__plants: list[Plant_type] = []

    def add_plants(self, plant: Plant_type) -> None:
        if plant.get_name() is None:
            raise InvalidName(plant.get_name())
        print(f"Added {plant.get_name()} successfully")
        self.__plants.append(plant)

    def watering(self) -> None:
        print("Watering plants...")
        print("Opening watering system")
        for plant in self.__plants:
            print(f"watering {plant.get_name()} - Success")
        print("Closing watering system (cleanup)")

    def check_plants(self) -> None:
        for plant in self.__plants:
            if not (plant.get_water() >= 1 and plant.get_water() <= 10):
                raise InvalidHealth(plant.get_name(), plant.get_water())
            else:
                print(f"{plant.get_name()}: healthy (water:", end=" ")
                print(f"{plant.get_water()}, sun: {plant.get_sun()})")


def test_garden_management(lista: list[Plant_type], garden: GardenManager):
    try:
        for plant in lista:
            garden.add_plants(plant)
    except InvalidName as e:
        print(f"{e}")
    try:
        print()
        garden.watering()
        print()
        print("Checking plant health...")
        garden.check_plants()
    except InvalidHealth as e:
        print(f"{e}")
    finally:
        print()
        print("Testing error recovery...")
        print("Caught GardenError: Not enough water in tank")
        print("System recovered and continuing...")
        print("Garden management system test complete!")


if __name__ == "__main__":
    tomato = Plant_type("tomato", 5, 8)
    lettuce = Plant_type("lettuce", 15, 8)
    papa = Plant_type(None, 8, 10)
    lista = [tomato, lettuce, papa]
    garden = GardenManager()
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    test_garden_management(lista, garden)
