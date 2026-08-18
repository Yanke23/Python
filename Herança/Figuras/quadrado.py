from figura import Figura

class Quadrado(Figura):
    def __init__(self, cor: str, lado: float):
        super().__init__(cor)
        self.__lado = lado

    def get_lado(self) -> float:
        return self.__lado

    def set_lado(self, lado: float):
        self.__lado = lado

    def calcular_area(self) -> float:
        return self.__lado ** 2