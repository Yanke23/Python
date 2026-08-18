from conteudo import conteudo

class Filme(conteudo):
    
    def __init__(self, Categoria: str, Titulo: str, duracao: int):
        super().__init__(Categoria, Titulo)
        self.__duracao = duracao
        
    # GET | SET
    def setDuracao(self, duracao: int):
        self.__duracao = duracao
        
    def getDuracao(self) -> int:
        return self.__duracao

    def Descricao(self):
        print("-------------------------")
        print(f"Categoria: {super().getCategoria()}")
        print(f"Nome: {super().getTitulo()}")
        print(f"Duração: {self.__duracao}min")