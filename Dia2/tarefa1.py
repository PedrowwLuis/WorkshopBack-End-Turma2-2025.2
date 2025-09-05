import math

numero = float(input("Digite um número: "))

def calcular_raiz(numero):
    if numero >= 0:
        raiz_quadrada = math.sqrt(numero)
        return f"A raiz quadrada de {numero} é {raiz_quadrada}"
    else:
        return "Não é possível calcular a raiz quadrada de um número negativo."

print(calcular_raiz(numero))
