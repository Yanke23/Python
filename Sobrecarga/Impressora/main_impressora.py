from impressora import Impressora

def main():
    imp = Impressora()

    print("--- Sistema de Impressão ---")
    
    # Chamando o método sem parâmetros
    imp.exibir_mensagem()

    # Chamando o método com 1 parâmetro
    imp.exibir_mensagem("Sistema iniciado com sucesso.")

    # Chamando o método com 2 parâmetros
    imp.exibir_mensagem("Rede", "Conexão estabelecida.")

    # Chamando o método com 3 ou mais parâmetros
    imp.exibir_mensagem("Erro", "Banco de Dados", "Timeout na conexão", 404)

if __name__ == "__main__":
    main()