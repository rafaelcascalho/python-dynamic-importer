from abc import ABC, abstractmethod


class BaseClass(ABC):
    @abstractmethod
    def say_fuck_you(self, s: str) -> str:
        pass
