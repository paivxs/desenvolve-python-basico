# Exercício 2 - Listas, soma e média 

import random

# gerar aleatoriamente um número entre 5 e 20 
num_elementos = random.randint(5, 20)

# criar a lista com num_elementos números aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# calcular soma e média
soma = sum(elementos)
media = soma / num_elementos

# imprime os resultados
print("Lista elementos:", elementos)
print("Soma dos valores da lista:", soma)
print("Média dos valores da lista:", media)