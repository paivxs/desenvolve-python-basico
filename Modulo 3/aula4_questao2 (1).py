# Questão 2

# Entrada de dados (Lê a nota do usuário)
nota = int(input("Digite a nota do filme (1 a 5): "))

# Verifica e imprime a mensagem correspondente
if nota == 5:
    print("Exelente!")
elif nota == 4:
    print("Muito bom!")
elif nota == 3:
    print("Bom!")
elif nota == 2:
    print("Regular.")
elif nota == 1:
    print("Ruim.")
else:
    print("Nota inválida. Digite um número de 1 a 5.")