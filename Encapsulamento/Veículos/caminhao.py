class Caminhao:
    def __init__(self, marca: str, modelo: str, capacidade_carga: float):
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidade_carga = capacidade_carga

    def get_marca(self) -> str: return self.__marca
    def set_marca(self, marca: str): self.__marca = marca
    
    def get_modelo(self) -> str: return self.__modelo
    def set_modelo(self, modelo: str): self.__modelo = modelo
    
    def get_capacidade_carga(self) -> float: return self.__capacidade_carga
    def set_capacidade_carga(self, capacidade: float): self.__capacidade_carga = capacidade

    def detalhes(self):
        print(f"[Caminhão] Marca: {self.__marca} | Modelo: {self.__modelo} | Carga: {self.__capacidade_carga} toneladas")