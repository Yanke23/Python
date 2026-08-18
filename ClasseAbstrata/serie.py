from conteudo import conteudo

class Serie(conteudo):
    
    def __init__(self, Categoria: str, Titulo: str, duracao: int, qntEps: int, qntTemps: int):
        super().__init__(Categoria, Titulo)
        self.__duracao = duracao
        self.__qntEps = qntEps
        self.__qntTemps = qntTemps
        
    # GET | SET
    def setDuracao(self, duracao: int):
        self.__duracao = duracao
        
    def getDuracao(self) -> int:
        return self.__duracao
        
    def setQntEps(self, qntEps: int):
        self.__qntEps = qntEps
        
    def getQntEps(self) -> int:
        return self.__qntEps
        
    def setQntTemps(self, qntTemps: int):
        self.__qntTemps = qntTemps
        
    def getQntTemps(self) -> int:
        return self.__qntTemps

    def Descricao(self):
        print("-------------------------")
        # Usando super() e os métodos get igual no Java
        print(f"Categoria: {super().getCategoria()}")
        print(f"Nome: {super().getTitulo()}")
        print(f"Duração Ep: {self.__duracao}min")
        print(f"Quantidade de Episódios: {self.__qntEps}")
        print(f"Quantidade de temporadas: {self.__qntTemps}\n")