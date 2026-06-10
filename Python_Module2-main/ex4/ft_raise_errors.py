def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif not (water_level >= 1 and water_level <= 10):
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif not (sunlight_hours >= 2 and sunlight_hours <= 12):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks(plant_name: str, water_level: int, sunlight_hours: int):
    try:
        check_plant_health(plant_name, water_level, sunlight_hours)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    print("")
    print("Testing good values...")
    test_plant_checks("tomato", 8, 8)
    print()
    print("Testing empty plant name...")
    test_plant_checks("", 8, 8)
    print()
    print("Testing bad water level...")
    test_plant_checks("tomato", 15, 8)
    print()
    print("Testing bad sunlight hours...")
    test_plant_checks("tomato", 5, 0)
    print()
    print("All error raising tests completed!")
