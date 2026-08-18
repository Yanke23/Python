class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        # Atributos privados (Encapsulamento)
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    # GETTERS
    def get_nome(self) -> str:
        return self.__nome

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    # SETTERS
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_preco(self, preco: float):
        if preco >= 0:  # Validação de dados no setter
            self.__preco = preco
        else:
            print("Preço não pode ser negativo.")

    def set_quantidade(self, quantidade: int):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            print("Quantidade não pode ser negativa.")

    def exibir_detalhes(self):
        print(f"Produto: {self.__nome} | Preço: R${self.__preco:.2f} | Estoque: {self.__quantidade}")