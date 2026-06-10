import abc

class CreatureAbstract(abc.ABC):
    def __init__(self, name: str, type: str) -> None:
        self._name = name
        self._type = type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creatura"
