from produto import Produto

class CarrinhoDeCompras:
    def __init__(self):
        self.__itens = [] # Vetor dinâmico

    def adicionar_produto(self, produto: Produto, quantidade: int):
        if produto.reduzir_estoque(quantidade):
            self.__itens.append({"produto": produto, "quantidade": quantidade})
            print(f"{quantidade}x {produto.get_nome()} adicionado ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto.get_nome()}.")

    def calcular_total(self) -> float:
        return sum(item["produto"].get_preco() * item["quantidade"] for item in self.__itens)

    def finalizar_compra(self):
        print("\n--- Cupom Fiscal ---")
        for item in self.__itens:
            p = item["produto"]
            q = item["quantidade"]
            print(f"{q}x {p.get_nome()} - R${p.get_preco() * q:.2f}")
        print(f"TOTAL: R${self.calcular_total():.2f}")
        print("--------------------")
        self.__itens.clear()