def pegar_valores_calculo(texto: str):
    numero1, operador, numero2 = texto.split()
    return float(numero1), operador, float(numero2)


def verificar_decimal(numero):
    numero = str(numero)
    parte_decimal = ""
    posicao = 0

    for posicao in range(0, len(numero)):
        if numero[posicao] == ".":
            parte_decimal = numero[posicao + 1 :]
            break

    if len(parte_decimal) == 1:
        numero = numero[:posicao]
        return int(numero)
    elif 7 > len(parte_decimal) > 1:  # para não ter imprecisão
        return float(numero)
    else:
        numero = int(f"{int(numero):.7f}")
        return numero


def fazer_calculos(numero1: float, operadores: str, numero2: float) -> str:
    match operadores:
        case "+":
            resposta = numero1 + numero2
        case "-":
            resposta = numero1 - numero2
        case "*" | "x" | "X":
            resposta = numero1 * numero2
        case "^" | "**":
            if numero1 != 0 and numero2 != 0:
                resposta = numero1**numero2
            else:
                resposta = "ERRO. EXPRESSÃO INDETERMINADA"
        case ":" | "/":
            if numero2 != 0:
                resposta = numero1 / numero2
            else:
                resposta = "ERRO. IMPOSSIVEL DIVIDIR POR ZERO"
        case _:
            resposta = "ERRO. EXPRESSÃO INVÁLIDA"

    if type(resposta) is not str:
        resposta = verificar_decimal(resposta)

    return str(resposta)
