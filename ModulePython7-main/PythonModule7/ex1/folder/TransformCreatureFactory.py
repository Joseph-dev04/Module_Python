from .transforming import Shiftling, Morphagon
from ex0.CreatureFactory import CreaturaFactory


class TransformCreatureFactory(CreaturaFactory):

    def create_base(self):
        return Shiftling()
    
    def create_evolved(self):
        return Morphagon()