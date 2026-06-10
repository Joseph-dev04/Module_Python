from ex1.folder.HealCapability import HealCapability
from ex1.folder.TransformCapability import TransformCapability
from .BattleStrategy import BattleStrategy, InvalidStrategyError
from ex0.CreatureAbstract import CreatureAbstract

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True
    
    def act(self, creature):
        print(creature.attack())

class AggresiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return isinstance(creature, TransformCapability)
    
    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid creature '{creature._name}' for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid creature '{creature._name}' for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
