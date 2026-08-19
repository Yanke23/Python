from animal import Animal

class Zoologico:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__jaulas = []

    def adicionar_animal(self, animal: Animal):
        self.__jaulas.append(animal)

    def alimentar_animais(self):
        print(f"\n=== Hora da alimentação no {self.__nome} ===")
        for animal in self.__jaulas:
            animal.emitir_som()

    def relatorio(self):
        print(f"\n=== Relatório de Animais - {self.__nome} ===")
        for animal in self.__jaulas:
            animal.detalhes()
            print("-" * 30)