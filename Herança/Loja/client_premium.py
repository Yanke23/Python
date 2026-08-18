from client import Client

class ClientPremium(Client):
    def __init__(self, nome: str, email: str, desconto: float):
        super().__init__(nome, email)
        self.__desconto = desconto

    def get_desconto(self) -> float:
        return self.__desconto

    def set_desconto(self, desconto: float):
        self.__desconto = desconto

    def detalhes(self):
        super().detalhes()
        print(f"Desconto Premium: {self.__desconto}%")