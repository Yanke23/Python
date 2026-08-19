from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str, idade: int, especie: str):
        self._nome = nome      # Protected (_)
        self._idade = idade
        self._especie = especie

    def get_nome(self) -> str:
        return self._nome

    @abstractmethod
    def emitir_som(self):
        pass

    def detalhes(self):
        print(f"{self.__class__.__name__}: {self._nome} | Idade: {self._idade} | Espécie: {self._especie}")