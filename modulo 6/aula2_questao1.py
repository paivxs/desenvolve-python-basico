# Exercício 1 - listas ordenação e índices

# importa a função para gerar números aleatórios 
import random

# cria uma lista com 20 números aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# cria uma versão ordenada da lista, sem modificar a original
lista_ordenada = sorted(lista)

# acha o índice do menor e maior valor
ind_maior = lista.index(max(lista))
ind_menor = lista.index(min(lista))

# imprime os resultados
print("Lista ordenada (sem modificar a original):", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", ind_maior)
print("Índice do menor valor:", ind_menor)