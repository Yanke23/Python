class Moto:
    def __init__(self, marca: str, modelo: str, cilindradas: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__cilindradas = cilindradas

    def get_marca(self) -> str: return self.__marca
    def set_marca(self, marca: str): self.__marca = marca
    
    def get_modelo(self) -> str: return self.__modelo
    def set_modelo(self, modelo: str): self.__modelo = modelo
    
    def get_cilindradas(self) -> int: return self.__cilindradas
    def set_cilindradas(self, cilindradas: int): self.__cilindradas = cilindradas

    def detalhes(self):
        print(f"[Moto] Marca: {self.__marca} | Modelo: {self.__modelo} | Cilindradas: {self.__cilindradas}cc")