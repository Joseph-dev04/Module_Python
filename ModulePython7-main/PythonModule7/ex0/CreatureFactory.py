import abc
class CreaturaFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self):
        pass
    @abc.abstractmethod
    def create_evolved(self):
        pass