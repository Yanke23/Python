from produto import Produto
from carrinho import CarrinhoDeCompras

def main():
    p1 = Produto(1, "Notebook", 4500.00, 5)
    p2 = Produto(2, "Mouse", 150.00, 20)
    p3 = Produto(3, "Teclado", 300.00, 2)

    carrinho = CarrinhoDeCompras()

    print("--- Produtos Disponíveis ---")
    p1.detalhes()
    p2.detalhes()
    p3.detalhes()
    print("\n")

    carrinho.adicionar_produto(p1, 1)
    carrinho.adicionar_produto(p3, 3) # Vai falhar (estoque = 2)
    carrinho.adicionar_produto(p3, 2) # Vai dar certo
    carrinho.adicionar_produto(p2, 2)

    carrinho.finalizar_compra()

if __name__ == "__main__":
    main()