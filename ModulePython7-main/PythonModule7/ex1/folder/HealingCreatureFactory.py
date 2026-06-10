from .healing import Sproutling, Bloomelle
from ex0.CreatureFactory import CreaturaFactory

class HealingCreatureFactory(CreaturaFactory):
    def create_base(self):
        return Sproutling()
    
    def create_evolved(self):
        return Bloomelle()
