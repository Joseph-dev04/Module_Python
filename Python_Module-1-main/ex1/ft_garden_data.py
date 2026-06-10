class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f" {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    planta1 = Plant("Rose", 25, 30)
    planta2 = Plant("Sunflower", 80, 45)
    planta3 = Plant("Cactus", 15, 120)
    print(" === Garden Plant Registry ===")
    planta1.show()
    planta2.show()
    planta3.show()
