import tkinter as tk


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


def verificar_decimal(numero : float):
        numero = str(numero)
        
        for posicao in range(0,len(numero)):
            if numero[posicao] == '.':
                parte_decimal = numero[posicao+1:] 
                break 
        
        if len(parte_decimal) == 1:
            numero = numero[:posicao]
            return int(numero)
        elif 7 > len(parte_decimal) > 1:
            return float(numero)
        else:
            numero = int(f'{numero:.7f}')
            return numero 


def fazer_calculos(numero1,operadores,numero2) -> str:
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
    
    if type(resposta) != str:
        resposta = verificar_decimal(resposta)   
    
    return resposta