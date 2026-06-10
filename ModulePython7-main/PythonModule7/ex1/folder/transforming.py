from .TransformCapability import TransformCapability
from ex0.CreatureAbstract import CreatureAbstract


class Shiftling(TransformCapability, CreatureAbstract):

    def __init__(self) -> None:
        CreatureAbstract.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)
    
    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        return f"{self._name} attacks normally!"
    
    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"
    
    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."

class Morphagon(TransformCapability, CreatureAbstract):
    def __init__(self) -> None:
        CreatureAbstract.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)
    
    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally!"
    
    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"
    
    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form"