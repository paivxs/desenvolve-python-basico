# Exercício 4 - Intercalar duas listas com quantidades diferentes de elementos

# recebe a quantidade de elementos da lista 1
qtd1 = int(input("Digite a quantidade de elementos da lista 1:" ))
lista1 = []

# recebe os elementos da lista 1 
print(f"Digite os {qtd1} elementos da lista 1: ")
for _ in range (qtd1):
    num = int(input())
    lista1.append(num)

# recebe a quantidade de elementos da lista 2
qtd2 = int(input("Digite a quantidade de elementos da lista 2:" ))
lista2 = []

# recebe os elementos da lista 2
print(f"Digite os {qtd2} elementos da lista 2: ")
for _ in range (qtd2):
    num = int(input())
    lista2.append(num)

# cria lista intercalada
intercalada = []

# pega o tamanho da maior lista 
tamanho_max = max(qtd1, qtd2)

# intercala os elementos das duas listas
for i in range(tamanho_max):
    if i < qtd1:
        intercalada.append(lista1[i])
    if i < qtd2:
        intercalada.append(lista2[i])

# mostra o resultado final
print("Lista intercalada:", *intercalada)
