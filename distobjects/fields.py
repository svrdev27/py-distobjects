from abc import ABC, abstractmethod

class AbstractField(ABC):
    @abstractmethod
    def serialize(self, value:object) -> str:
        pass

    @abstractmethod
    def deserialize(self, value:str) -> object:
        pass

class TextField(AbstractField):
    def serialize(self, value:str) -> str:
        return value

    def deserialize(self, value:str) -> str:
        return value