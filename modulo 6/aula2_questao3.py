# Exercício 3 - Interseção de listas

import random

# cria duas listas com 20 números aleatórios de 0 a 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# encontra a interseção das listas (sem duplicados)
intersecao = sorted(set(lista1) & set(lista2))

# mostra as listas e a interseção
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("\nInterseção (ordenada sem duplicadas):", intersecao)

# mostra quantas vezes cada número da interseção aparece em cada lista
print("\nContagem de repetições na interseção:")
for numero in intersecao:
    cont1 = lista1.count(numero)
    cont2 = lista2.count(numero)
    print(f"{numero}: (lista1 = {cont1}, lista2 = {cont2})")