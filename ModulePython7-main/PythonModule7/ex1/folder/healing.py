from ex0.CreatureAbstract import CreatureAbstract
from .HealCapability import HealCapability


class Sproutling(CreatureAbstract, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Heal")

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"
    
    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"
    

class Bloomelle(CreatureAbstract, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Heal")
    
    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"
    
    def heal(self):
        return f"{self._name} heals itself and others for a large amount"