from figura import Figura

class Losango(Figura):
    def __init__(self, cor: str, diagonal_maior: float, diagonal_menor: float):
        super().__init__(cor)
        self.__diagonal_maior = diagonal_maior
        self.__diagonal_menor = diagonal_menor

    def get_diagonal_maior(self) -> float:
        return self.__diagonal_maior

    def set_diagonal_maior(self, diagonal_maior: float):
        self.__diagonal_maior = diagonal_maior

    def get_diagonal_menor(self) -> float:
        return self.__diagonal_menor

    def set_diagonal_menor(self, diagonal_menor: float):
        self.__diagonal_menor = diagonal_menor

    def calcular_area(self) -> float:
        return (self.__diagonal_maior * self.__diagonal_menor) / 2