class Client:
    def __init__(self, nome: str, email: str):
        self.__nome = nome
        self.__email = email

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def detalhes(self):
        print(f"Cliente: {self.__nome} | Email: {self.__email}")