from animal import Animal

class Mamifero(Animal):
    def __init__(self, nome: str, idade: int, especie: str, cor_pelo: str):
        super().__init__(nome, idade, especie)
        self.__cor_pelo = cor_pelo

    def emitir_som(self):
        print(f"O mamífero {self._nome} está rugindo/grunhindo!")

    def detalhes(self):
        super().detalhes()
        print(f"  └─ Pelagem: {self.__cor_pelo}")