from quadrado import Quadrado
from retangulo import Retangulo
from triangulo import Triangulo
from losango import Losango

def main():
    q = Quadrado("Vermelho", 5.0)
    r = Retangulo("Azul", 4.0, 6.0)
    t = Triangulo("Verde", 3.0, 8.0)
    l = Losango("Amarelo", 6.0, 4.0)

    figuras = [q, r, t, l]

    print("--- Cálculo de Área das Figuras ---")
    for fig in figuras:
        print(f"Forma: {fig.__class__.__name__} | Cor: {fig.get_cor()} | Área: {fig.calcular_area():.2f}")

if __name__ == "__main__":
    main()