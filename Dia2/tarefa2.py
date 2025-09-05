import math

n1 = float(input("Digite um número para ser arredondado: "))

def arredondamentos(n1):
    piso = math.floor(n1)
    teto = math.ceil(n1)
    arredondamento = round(n1)
    return (f"Seu Número arredondado para cima é {teto}, seu número arredondado para baixo é: {piso}, e seu número arredondado é: {arredondamento}")

print(arredondamentos(n1))