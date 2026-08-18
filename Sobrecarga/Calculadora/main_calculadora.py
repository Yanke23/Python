from calculadora import Calculadora

def main():
    calc = Calculadora()

    # Chamando o "mesmo" método com assinaturas (quantidades de parâmetros) diferentes
    soma_dois = calc.somar(10.0, 5.0)
    soma_tres = calc.somar(10.0, 5.0, 2.0)

    mult_dois = calc.multiplicar(2.0, 4.0)
    mult_tres = calc.multiplicar(2.0, 4.0, 3.0)

    print("--- Calculadora (Sobrecarga) ---")
    print(f"Soma de 2 números: {soma_dois}")
    print(f"Soma de 3 números: {soma_tres}")
    print(f"Multiplicação de 2 números: {mult_dois}")
    print(f"Multiplicação de 3 números: {mult_tres}")

if __name__ == "__main__":
    main()