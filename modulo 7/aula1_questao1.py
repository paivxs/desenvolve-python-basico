# Atividade 1 - Nome em escada

# solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# cria um laço de repetição que vai de 1 até o comprimento do nome
for i in range(1, len(nome) + 1):

# imprime os primeiros (i) caracteres do nome
    print(nome[:i])

