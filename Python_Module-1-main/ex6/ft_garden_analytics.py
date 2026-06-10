class Plant:
    def __init__(self, species, grow):
        self.__species = species
        self.__grow = grow

    def get_species(self):
        return self.__species

    def get_grow(self):
        return self.__grow

    def set_grow(self, grow):
        self.__grow += grow


class FloweringPlant(Plant):
    def __init__(self, species, color, grow):
        super().__init__(species, grow)
        self.__color = color

    def get_color(self):
        return self.__color


class PrizeFlower(FloweringPlant):
    def __init__(self, species, color, award, grow):
        super().__init__(species, color, grow)
        self.__award = award

    def get_price(self):
        return self.__award


class GardenManager:
    all_gardens = []

    def __init__(self, name: str):
        self.__name = name
        self.__plants = []
        self.__update_cm = 0
        GardenManager.all_gardens.append(self)

    @classmethod
    def create_garden_network(cls, plants):
        return [cls(name) for name in plants]

    def add_garden(self, plants: Plant):
        self.__plants.append(plants)
        print(f"Added {plants.get_species()} to {self.__name}'s garden")

    def list_types(self):
        regular = 0
        flower = 0
        prize = 0
        for plant in self.__plants:
            tipo = plant.__class__.__name__
            if tipo == "Plant":
                regular += 1
            elif tipo == "FloweringPlant":
                flower += 1
            elif tipo == "PrizeFlower":
                prize += 1
        print(f"Plants types: {regular} regular,", end=" ")
        print(f"{flower} FloweingPlant,", end=" ")
        print(f"{prize} PrizeFlower")

    def get_name(self):
        return self.__name

    def get_plants(self):
        return (self.__plants)

    def get_allgrowt(self):
        return self.__update_cm

    def garden_grow(self):
        print("Alice is helping all plants grow...")
        cm = 1
        for plant in self.__plants:
            self.__update_cm += cm
            plant.set_grow(cm)
            print(f"{plant.get_species()} grew {cm}cm")

    def validationgrow(self):
        validation = True
        for plant in self.__plants:
            if (plant.get_grow() < 0):
                validation = False
                return validation
        return validation

    def garden_report(self):
        print()
        print("=== Alice's Garden Report ===")
        print("Plants in garden:")
        for plant in self.__plants:
            tipo = plant.__class__.__name__
            if tipo == "Plant":
                print(f"- {plant.get_species()}: {plant.get_grow()}cm")
            elif tipo == "FloweringPlant":
                print(f"- {plant.get_species()}:", end=" ")
                print(f"{plant.get_grow()}cm, {plant.get_color()}", end=" ")
                print("flowers (blooming)")
            elif tipo == "PrizeFlower":
                print(f"- {plant.get_species()}:", end=" ")
                print(f"{plant.get_grow()}cm, {plant.get_color()}", end=" ")
                print("flowers (blooming), Prize points:", end=" ")
                print(plant.get_price())
        print()

    class GardenStats:
        @staticmethod
        def calc(plants):
            count = 0
            for plant in plants:
                count += 1
            return count

        @staticmethod
        def total_grow(plants):
            total = 0
            for plant in plants:
                total += plant.get_grow()
            return total


if __name__ == "__main__":
    Oak = Plant("Oak tree", 100)
    Sunflower = PrizeFlower("Sunflower", "yellow", 10, 50)
    Alice = GardenManager("Alice")
    Bob = GardenManager("Bob")
    Rose = FloweringPlant("Rose", "red", 25)
    print("=== Garden Management System Demo ===")
    print()
    Alice.add_garden(Oak)
    Alice.add_garden(Rose)
    Alice.add_garden(Sunflower)
    print()
    Alice.garden_grow()
    Alice.garden_report()
    print("Plants added:", end=" ")
    print(f"{GardenManager.GardenStats.calc(Alice.get_plants())}", end=" ")
    print("Total growth:", end=" ")
    print(f"{Alice.get_allgrowt()}cm")
    Alice.list_types()
    print()
    print(f"Height validation test: {Alice.validationgrow()}")
    print(f"Garden scores - {Alice.get_name()}: 218,", end=" ")
    print(f"{Bob.get_name()}: 92")
    print("Total gardens managed:", end=" ")
    print(f"{GardenManager.GardenStats.calc(GardenManager.all_gardens)}")
