from abc import ABC, abstractmethod

class conteudo(ABC):
    
    # CONSTRUTOR
    def __init__(self, Categoria: str, Titulo: str):
        self.__Categoria = Categoria
        self.__Titulo = Titulo
        
    # GET | SET
    def setCategoria(self, Categoria: str):
        self.__Categoria = Categoria
        
    def getCategoria(self) -> str:
        return self.__Categoria
        
    def setTitulo(self, Titulo: str):
        self.__Titulo = Titulo
        
    def getTitulo(self) -> str:
        return self.__Titulo
        
    # METODOS
    @abstractmethod
    def Descricao(self):
        pass