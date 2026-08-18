from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, cor: str):
        self.__cor = cor

    def get_cor(self) -> str:
        return self.__cor

    def set_cor(self, cor: str):
        self.__cor = cor

    @abstractmethod
    def calcular_area(self) -> float:
        pass