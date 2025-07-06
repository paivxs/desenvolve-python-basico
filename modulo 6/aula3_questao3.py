# Exercício 3

import random # importa o modulo para gerar números aleatórios 

# cria a lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-1, 10) for _ in range(20)]

# imprime a lista original
print("Lista original:", lista)

# encontra o intervalo com mais números negativos
maior_qtd_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

# percorre todos os intervalos possíveis da lista
for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        intervalo = lista[i:j]
        qtd_negativos = len([x for x in intervalo if x < 0])

# remove da lista o intervalo com mais números negativos
del lista [inicio_intervalo:fim_intervalo]

# imprime a lista após deletar o intervalo
print("Lista editada:", lista)