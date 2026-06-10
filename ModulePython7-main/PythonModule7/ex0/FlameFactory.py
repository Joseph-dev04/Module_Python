from .CreatureFactory import CreaturaFactory
from .flame import Pyrodon, Flameling
class FlameFactory(CreaturaFactory):
    def create_base(self):
        return Flameling()
    
    def create_evolved(self):
        return Pyrodon()