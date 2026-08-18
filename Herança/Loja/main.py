from client import Client
from client_premium import ClientPremium

def main():
    cliente_comum = Client("João Silva", "joao@email.com")
    cliente_premium = ClientPremium("Maria Souza", "maria@email.com", 15.0)

    print("--- Cliente Padrão ---")
    cliente_comum.detalhes()

    print("\n--- Cliente Premium ---")
    cliente_premium.detalhes()

if __name__ == "__main__":
    main()