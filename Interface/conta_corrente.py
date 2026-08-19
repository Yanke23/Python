from conta import Conta
from tributo import Tributo

class ContaCorrente(Conta, Tributo):
    def __init__(self, numero: int, titular: str, saldo: float = 0.0, taxa_manutencao: float = 12.0):
        super().__init__(numero, titular, saldo)
        self.__taxa_manutencao = taxa_manutencao

    def calcular_tributo(self) -> float:
        # Taxa de 1% sobre o saldo + tarifa de manutenção
        return (self.get_saldo() * 0.01) + self.__taxa_manutencao

    def exibir_dados(self):
        super().exibir_dados()
        print(f"  └─ Categoria: Conta Corrente | Imposto Estimado: R${self.calcular_tributo():.2f}")