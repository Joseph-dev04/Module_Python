class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, upgrade: int):
        self.height += upgrade

    def ft_age(self, days: int):
        self.age += days

    def get_info(self, upgrade: int):
        self.grow(upgrade)
        self.ft_age(upgrade)
        print(f" === Day {upgrade + 1} ===")
        self.show()
        print(f" Growth this week: +{upgrade}cm")

    def show(self):
        print(f" {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print(" ===Day 1 ===")
    planta1 = Plant("Rose", 25, 30)
    planta1.show()
    planta1.get_info(6)
