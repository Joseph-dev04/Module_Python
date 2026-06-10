class InvalidPlants(Exception):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__message = f"Cannot water {name} - invalid plant!"
        super().__init__(self.__message)


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant == "None":
            raise InvalidPlants(plant)
        print(f"Watering {plant}")


def test_watering_system(plants: list) -> None:

    try:
        water_plants(plants)
    except InvalidPlants as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    plants = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    test_watering_system(plants)
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    plants = ["tomato", "None"]
    test_watering_system(plants)
    print()
    print("Cleanup always happens, even with errors!")
