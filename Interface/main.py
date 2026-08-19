from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from conta_premium import ContaPremium

def buscar_conta(contas, numero):
    for c in contas:
        if c.get_numero() == numero:
            return c
    return None

def main():
    contas = []
    gerador_numero = 1001

    while True:
        print("\n=================================")
        print("      SISTEMA BANCÁRIO      ")
        print("=================================")
        print("1. Criar Conta Corrente")
        print("2. Criar Conta Poupança")
        print("3. Criar Conta Premium")
        print("4. Depositar")
        print("5. Sacar")
        print("6. Listar Todas as Contas")
        print("7. Aplicar Rendimentos (Poupanças)")
        print("0. Sair")
        print("---------------------------------")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titular = input("Nome do titular: ")
            saldo_inicial = float(input("Saldo inicial (R$): "))
            conta = ContaCorrente(gerador_numero, titular, saldo_inicial)
            contas.append(conta)
            print(f"\n[Sucesso] Conta Corrente N° {gerador_numero} criada!")
            gerador_numero += 1

        elif opcao == "2":
            titular = input("Nome do titular: ")
            saldo_inicial = float(input("Saldo inicial (R$): "))
            conta = ContaPoupanca(gerador_numero, titular, saldo_inicial)
            contas.append(conta)
            print(f"\n[Sucesso] Conta Poupança N° {gerador_numero} criada!")
            gerador_numero += 1

        elif opcao == "3":
            titular = input("Nome do titular: ")
            saldo_inicial = float(input("Saldo inicial (R$): "))
            conta = ContaPremium(gerador_numero, titular, saldo_inicial)
            contas.append(conta)
            print(f"\n[Sucesso] Conta Premium N° {gerador_numero} criada!")
            gerador_numero += 1

        elif opcao == "4":
            num = int(input("Informe o número da conta: "))
            conta = buscar_conta(contas, num)
            if conta:
                valor = float(input("Valor do depósito (R$): "))
                if conta.depositar(valor):
                    print("[Sucesso] Depósito realizado!")
                else:
                    print("[Erro] Valor inválido.")
            else:
                print("[Erro] Conta não encontrada.")

        elif opcao == "5":
            num = int(input("Informe o número da conta: "))
            conta = buscar_conta(contas, num)
            if conta:
                valor = float(input("Valor do saque (R$): "))
                if conta.sacar(valor):
                    print("[Sucesso] Saque realizado!")
                else:
                    print("[Erro] Saldo ou limite insuficiente.")
            else:
                print("[Erro] Conta não encontrada.")

        elif opcao == "6":
            print("\n--- RELAÇÃO DE CONTAS ---")
            if not contas:
                print("Nenhuma conta cadastrada.")
            else:
                for c in contas:
                    c.exibir_dados()
                    print("-" * 30)

        elif opcao == "7":
            houve_aplicacao = False
            for c in contas:
                if isinstance(c, ContaPoupanca):
                    rendimento = c.aplicar_rendimento()
                    print(f"Conta {c.get_numero()} ({c.get_titular()}): +R${rendimento:.2f} rendidos.")
                    houve_aplicacao = True
            if not houve_aplicacao:
                print("Nenhuma Conta Poupança cadastrada para aplicar rendimentos.")

        elif opcao == "0":
            print("\nEncerrando sistema... Até logo!")
            break

        else:
            print("\n[Erro] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()