from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero: int, titular: str, saldo: float = 0.0, taxa_rendimento: float = 0.006):
        super().__init__(numero, titular, saldo)
        self.__taxa_rendimento = taxa_rendimento

    def aplicar_rendimento(self):
        rendimento = self.get_saldo() * self.__taxa_rendimento
        self.depositar(rendimento)
        return rendimento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"  └─ Categoria: Conta Poupança | Rendimento Atual: {self.__taxa_rendimento * 100:.1f}% a.m.")