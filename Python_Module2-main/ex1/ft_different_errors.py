def garden_operations(error_type: str) -> int:
    if error_type == "value":
        return int("abc")
    elif error_type == "zero":
        return 10 / 0
    elif error_type == "file":
        with open("missing", "r") as f:
            return f.read
    elif error_type == "key":
        garden = {"rosas": 5, "tulipanes": 6}
        return garden["missing"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    try:
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        print()
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        print()
    try:
        print("Testing FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
        print()
    try:
        print("Testing KeyError...")
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
        print()
    print("Testing multiple errors together...")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
