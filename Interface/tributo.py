from abc import ABC, abstractmethod

class Tributo(ABC):
    @abstractmethod
    def calcular_tributo(self) -> float:
        pass