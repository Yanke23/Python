from funcionario import Funcionario

def main():
    func = Funcionario("Carlos Silva", 3000.00)

    print(f"--- Pagamentos: {func.get_nome()} ---")
    
    # Sobrecarga 1: Sem parâmetros adicionais (apenas salário base)
    pagamento_padrao = func.calcular_pagamento()
    print(f"Pagamento Padrão: R${pagamento_padrao:.2f}")

    # Sobrecarga 2: Apenas com bônus
    pagamento_com_bonus = func.calcular_pagamento(500.00)
    print(f"Pagamento com Bônus: R${pagamento_com_bonus:.2f}")

    # Sobrecarga 3: Com bônus e descontos
    pagamento_final = func.calcular_pagamento(500.00, 200.00)
    print(f"Pagamento Final (Bônus + Desconto): R${pagamento_final:.2f}")

if __name__ == "__main__":
    main()