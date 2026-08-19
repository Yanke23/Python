from animal import Animal

class Ave(Animal):
    def __init__(self, nome: str, idade: int, especie: str, voa: bool):
        super().__init__(nome, idade, especie)
        self.__voa = voa

    def emitir_som(self):
        print(f"A ave {self._nome} está cantando/piando!")

    def detalhes(self):
        super().detalhes()
        habilidade = "Pode voar" if self.__voa else "Não voa"
        print(f"  └─ Habilidade: {habilidade}")