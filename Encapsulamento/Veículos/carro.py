class Carro:
    def __init__(self, marca: str, modelo: str, portas: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__portas = portas

    def get_marca(self) -> str: return self.__marca
    def set_marca(self, marca: str): self.__marca = marca
    
    def get_modelo(self) -> str: return self.__modelo
    def set_modelo(self, modelo: str): self.__modelo = modelo
    
    def get_portas(self) -> int: return self.__portas
    def set_portas(self, portas: int): self.__portas = portas

    def detalhes(self):
        print(f"[Carro] Marca: {self.__marca} | Modelo: {self.__modelo} | Portas: {self.__portas}")