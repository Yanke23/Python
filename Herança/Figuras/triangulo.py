from figura import Figura

class Triangulo(Figura):
    def __init__(self, cor: str, base: float, altura: float):
        super().__init__(cor)
        self.__base = base
        self.__altura = altura

    def get_base(self) -> float:
        return self.__base

    def set_base(self, base: float):
        self.__base = base

    def get_altura(self) -> float:
        return self.__altura

    def set_altura(self, altura: float):
        self.__altura = altura

    def calcular_area(self) -> float:
        return (self.__base * self.__altura) / 2