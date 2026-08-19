class Conta:
    def __init__(self, numero: int, titular: str, saldo: float = 0.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    def get_numero(self) -> int:
        return self.__numero

    def get_titular(self) -> str:
        return self.__titular

    def get_saldo(self) -> float:
        return self.__saldo

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def exibir_dados(self):
        print(f"Nº Conta: {self.__numero} | Titular: {self.__titular} | Saldo: R${self.__saldo:.2f}")