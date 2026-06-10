class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f" Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print(" === Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    plant_list = [plant1, plant2, plant3, plant4, plant5]
    i = 0
    while (i < 5):
        plant_list[i].show()
        i += 1
    print()
    print(f" Total plants created: {i}")
