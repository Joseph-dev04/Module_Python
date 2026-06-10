class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


class Vegetable(Plant):
    def __init__(self, seas: str, nutr: str, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.__harvest_season = seas
        self.__nutritional_value = nutr

    def get_season(self) -> str:
        return self.__harvest_season

    def get_nutriti(self) -> str:
        return self.__nutritional_value


class Flower(Plant):
    def __init__(self, color: str, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.__color = color

    def bloom(self):
        print(f"{self._name} is blooming beautifully!")

    def get_color(self):
        return self.__color


class Tree(Plant):
    def __init__(self, trunk_diameter: int, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self._name} provides 78", end=" ")
        print(" square meters of shade")

    def get_diameter(self):
        return self.__trunk_diameter


if __name__ == "__main__":
    rose = Flower("red", "Rose", 25, 30)
    oak = Tree(50, "Oak", 500, 1825)
    tomato = Vegetable("summer harvest", "C", "Tomato", 80, 90)
    print(" === Garden Plant Types ===")
    print()
    print(f"{rose.get_name()} (Flower): {rose.get_height()}cm,", end=" ")
    print(f"{rose.get_age()} days {rose.get_color()} color")
    rose.bloom()
    print()
    print(f"{oak.get_name()} (Tree): {oak.get_height()}cm,", end=" ")
    print(f"{oak.get_age()} days {oak.get_diameter()}cm diameter")
    oak.produce_shade()
    print()
    print(f"{tomato.get_name()} (Vegetable): {tomato.get_height()}cm", end=" ")
    print(f", {tomato.get_age()} days, {tomato.get_season()}")
    print(f"{tomato.get_name()} is rich in vitamin {tomato.get_nutriti()}")
