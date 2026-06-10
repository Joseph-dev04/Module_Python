from .CreatureAbstract import CreatureAbstract

class Aquabub(CreatureAbstract):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self._name} uses water Gun!"

class Torragon(CreatureAbstract):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"