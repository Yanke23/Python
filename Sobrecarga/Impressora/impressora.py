class Impressora:
    # Sobrecarga utilizando *args para aceitar de 1 a N parâmetros
    def exibir_mensagem(self, *args):
        quantidade = len(args)

        if quantidade == 1:
            print(f"[Aviso] {args[0]}")
        elif quantidade == 2:
            print(f"[Detalhe] Categoria: {args[0]} | Mensagem: {args[1]}")
        elif quantidade > 2:
            texto_unido = " - ".join(map(str, args))
            print(f"[Log Completo] {texto_unido}")
        else:
            print("[Vazio] Nenhuma mensagem fornecida.")