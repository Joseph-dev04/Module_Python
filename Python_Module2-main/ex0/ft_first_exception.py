def check_temperature(temp_str: str) -> int:
    try:
        number = int(temp_str)
        if number >= 0 and number <= 40:
            print(f"Temperature {number}°C is perfect for plants!")
            return number
        else:
            print(f"Error: {number}°C is too hot for plants (max 40°C)")
            return 0
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    number = input("")
    print()
    print(f"Testing temperature: {number}")
    check_temperature(number)


if __name__ == "__main__":
    print("=== Garden temperature Checker ===")
    test_temperature_input()
    test_temperature_input()
    test_temperature_input()
