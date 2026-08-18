class Calculadora:
    # Em Python, a sobrecarga de métodos é feita utilizando valores padrão (None, 0, etc.)
    def somar(self, a: float, b: float, c: float = None) -> float:
        if c is not None:
            return a + b + c
        return a + b

    def multiplicar(self, a: float, b: float, c: float = None) -> float:
        if c is not None:
            return a * b * c
        return a * b