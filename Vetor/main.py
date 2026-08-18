from produto import Produto

def main():
    # Vetor dinâmico padrão do Python (Lista)
    vetor_dinamico = []
    
    vetor_dinamico.append(Produto("Notebook", 3500.00))
    vetor_dinamico.append(Produto("Mouse", 120.50))
    vetor_dinamico.append(Produto("Teclado", 250.00))

    # Vetor de tamanho fixo (Lógica similar ao Java: Produto[] vetor = new Produto[3];)
    vetor_fixo = [None] * 3
    
    vetor_fixo[0] = Produto("Monitor", 1200.00)
    vetor_fixo[1] = Produto("Cadeira", 850.00)
    vetor_fixo[2] = Produto("Mesa", 500.00)

    print("--- Vetor Dinâmico ---")
    for produto in vetor_dinamico:
        produto.detalhes()

    print("\n--- Vetor Fixo (Acesso por Índice) ---")
    for i in range(len(vetor_fixo)):
        vetor_fixo[i].detalhes()

if __name__ == "__main__":
    main()