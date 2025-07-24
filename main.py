import funcoes

def main():
    valor_usuario = input()
    numero1 , operador , numero2 = funcoes.pegar_valores_calculo(valor_usuario) 
    print(resposta := funcoes.fazer_calculos(numero1,
                                             operador,
                                             numero2))

if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break    
    