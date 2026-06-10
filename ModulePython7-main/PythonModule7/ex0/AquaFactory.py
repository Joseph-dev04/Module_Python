from .CreatureFactory import CreaturaFactory
from .aqua import Aquabub, Torragon
class AquaFactory(CreaturaFactory):
    def create_base(self):
        return Aquabub()
    
    def create_evolved(self):
        return Torragon()