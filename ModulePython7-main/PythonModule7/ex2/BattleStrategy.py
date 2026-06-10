import abc

class InvalidStrategyError(Exception):
    pass

class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    def act(self, creature) -> None:
        pass