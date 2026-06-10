class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self) -> str:
        return self.__name

    def set_height(self, new_height):
        if new_height < 0:
            print("Invalid operation attemped: height", end=" ")
            print(f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height

    def set_age(self, new_age):
        if new_age < 0:
            print("Invalid operation attemped: height", end=" ")
            print(f"{new_age} days [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__age = new_age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    planta = Plant("Rose", 10, 10)
    planta.set_age(30)
    planta.set_height(25)
    print(f"Plant created: {planta.get_name()}")
    print(f"Height updated: {planta.get_height()}cm [OK]")
    print(f"Age updated: {planta.get_age()} days [OK]")
    print()
    planta.set_height(-5)
    print()
    print(f"Current plant: {planta.get_name()}", end=" ")
    print(f"({planta.get_height()}cm, {planta.get_age()} days)")
