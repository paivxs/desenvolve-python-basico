# atividade 2 - Gera n números aleatórios entre 0 e 100 e calcula a raiz quadrada da soma

import random
import math

# pede ao usuário o valor de n
n = int(input("Digite a quantidade de números aleatórios: "))

# gera os números e calcula a soma 
soma = 0 
for _ in range(n):
    numero = random.randint(0, 100)
    soma += numero
    print(f"Número gerado: {numero}")

# calcula a raiz quadrada da soma
raiz = math.sqrt(soma)

# exibe o resultado
print(f"Soma dos números: {soma}")
print(f"Raiz quadrada da soma: {round(raiz,2)}")