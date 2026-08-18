from produto import Produto

def main():
    p1 = Produto("Notebook", 3500.00, 10)
    p1.exibir_detalhes()

    # Utilizando os métodos SET para alterar os atributos encapsulados
    p1.set_preco(3200.00)
    p1.set_quantidade(8)
    
    # Utilizando os métodos GET para acessar os atributos encapsulados
    print(f"Novo preço do {p1.get_nome()}: R${p1.get_preco():.2f}")

if __name__ == "__main__":
    main()