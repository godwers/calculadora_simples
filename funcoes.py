def pegar_valores_calculo(texto : str):
    tamanho_texto = len(texto)  
    primeiro_espaco = 0
    numero1 = 0
    operador = ''
    numero2 = 0
    
    for posicao in range(0,tamanho_texto):
        if texto[posicao] == " " and primeiro_espaco == 0: 
            primeiro_espaco = posicao
            numero1 = float(texto[:posicao])
        elif texto[posicao] == " " and primeiro_espaco != 0:
            operador = texto[primeiro_espaco:posicao]
            operador = operador.strip()
        if texto[posicao] == " " and posicao != primeiro_espaco:
            numero2 = float(texto[posicao:tamanho_texto])
    return numero1 , operador , numero2
    
    
def fazer_calculos(numero1,operadores,numero2) -> float:
    match operadores:
        case '+':
            resposta = numero1 + numero2
        case '-':
            resposta = numero1 - numero2
        case '*' | 'x' | 'X':
            resposta = numero1 * numero2
        case '**' | '^':
            if numero1 != 0 and numero2 != 0:
                resposta = numero1 ** numero2
            else:
                resposta = "ERRO. EXPRESSÃO INDETERMINADA"
        case ':' | '/':
            if numero2 != 0:
                resposta = numero1 / numero2
            else:
                resposta = "ERRO. IMPOSSIVEL DIVIDIR POR ZERO"
        case "//":
            resposta = numero1 // numero2
        case _:
            resposta = "ERRO. EXPRESSÃO INVÁLIDA"
    return resposta