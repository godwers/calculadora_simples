import funcoes


def main():
    valor_usuario = input()
    numero1, operador, numero2 = funcoes.pegar_valores_calculo(valor_usuario)
    resposta = funcoes.fazer_calculos(numero1, operador, numero2)
    print(resposta)


if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            break
        except KeyboardInterrupt:
            break
    print("Encerrando a calculadora.")
