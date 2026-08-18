from carro import Carro
from moto import Moto
from caminhao import Caminhao

def main():
    meu_carro = Carro("Toyota", "Corolla", 4)
    minha_moto = Moto("Honda", "CB 500", 500)
    meu_caminhao = Caminhao("Volvo", "FH 540", 30.0)

    # Exibindo detalhes iniciais
    meu_carro.detalhes()
    minha_moto.detalhes()
    meu_caminhao.detalhes()

    print("\n--- Atualizando dados via Encapsulamento ---")
    
    # Modificando via Setters
    meu_carro.set_portas(2)
    minha_moto.set_cilindradas(600)
    
    # Acessando via Getters
    print(f"O carro {meu_carro.get_modelo()} agora tem {meu_carro.get_portas()} portas.")
    print(f"A moto {minha_moto.get_modelo()} sofreu upgrade para {minha_moto.get_cilindradas()}cc.")

if __name__ == "__main__":
    main()