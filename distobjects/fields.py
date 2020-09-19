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
        if value is not None:
            value = value.encode('utf-8')
        return value

    def deserialize(self, value:str) -> str:
        if value is not None:
            value = value.decode('utf-8')
        return value
