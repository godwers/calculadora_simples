import funcoes


def main():
    valor_usuario = input()
    numero1 , operador , numero2 = funcoes.pegar_valores_calculo(valor_usuario)
    #print(numero1,operador,numero2) 
    resposta = funcoes.fazer_calculos(numero1,operador,numero2)
    print(f'{resposta:.7f}')

if __name__ == '__main__':
    main()
    
    