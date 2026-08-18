class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self) -> str:
        return self.__nome

    def get_preco(self) -> float:
        return self.__preco

    def detalhes(self):
        print(f"Produto: {self.__nome} | Preço: R${self.__preco:.2f}")