class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.__nome = nome
        self.__salario_base = salario_base

    def get_nome(self) -> str:
        return self.__nome

    # Sobrecarga utilizando valores padrão (default arguments)
    def calcular_pagamento(self, bonus: float = 0.0, descontos: float = 0.0) -> float:
        return self.__salario_base + bonus - descontos