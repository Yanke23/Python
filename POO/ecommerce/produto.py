class Produto:
    def __init__(self, codigo: int, nome: str, preco: float, estoque: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def get_nome(self) -> str: return self.__nome
    def get_preco(self) -> float: return self.__preco
    def get_estoque(self) -> int: return self.__estoque

    def reduzir_estoque(self, quantidade: int) -> bool:
        if 0 < quantidade <= self.__estoque:
            self.__estoque -= quantidade
            return True
        return False

    def repor_estoque(self, quantidade: int):
        self.__estoque += quantidade

    def detalhes(self):
        print(f"[{self.__codigo}] {self.__nome} - R${self.__preco:.2f} (Estoque: {self.__estoque})")