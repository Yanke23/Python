from conta import Conta
from tributo import Tributo

class ContaPremium(Conta, Tributo):
    def __init__(self, numero: int, titular: str, saldo: float = 0.0, limite: float = 2000.0, cashback_rate: float = 0.02):
        super().__init__(numero, titular, saldo)
        self.__limite = limite
        self.__cashback_rate = cashback_rate

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            cashback = valor * self.__cashback_rate
            super().depositar(valor + cashback)
            print(f"   [Bônus Premium] Cashback aplicado: +R${cashback:.2f}")
            return True
        return False

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= (self.get_saldo() + self.__limite):
            # Abatimento priorizando o saldo antes do limite
            saldo_atual = self.get_saldo()
            if valor <= saldo_atual:
                super().sacar(valor)
            else:
                excedente = valor - saldo_atual
                super().sacar(saldo_atual)
                self.__limite -= excedente
            return True
        return False

    def calcular_tributo(self) -> float:
        # Clientes Premium pagam alíquota reduzida (0.5%)
        return self.get_saldo() * 0.005

    def exibir_dados(self):
        super().exibir_dados()
        print(f"  └─ Categoria: Conta Premium | Limite: R${self.__limite:.2f} | Imposto Estimado: R${self.calcular_tributo():.2f}")