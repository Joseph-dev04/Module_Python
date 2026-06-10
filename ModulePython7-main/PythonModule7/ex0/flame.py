from .CreatureAbstract import CreatureAbstract

class Flameling(CreatureAbstract):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")
    
    def attack(self) -> str:
        return f"{self._name} uses Ember!"
    
class Pyrodon(CreatureAbstract):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"
