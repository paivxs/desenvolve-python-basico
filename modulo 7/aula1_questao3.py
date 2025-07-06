# Atividade 3 - Conta palavras em uma frase

# solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# usa o método split() para dividir a frase em palavras, separando pelos espaços
palavras = frase.split()

# conta quantas palavras tem na lista
quantidade = len(palavras)

# mostra a quantidade
print("Espaços em branco:", quantidade - 1)
print("Número de palavras:", quantidade)