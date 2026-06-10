import abc

class TransformCapability(abc.ABC):

    def __init__(self):
        self._transformed = False

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass