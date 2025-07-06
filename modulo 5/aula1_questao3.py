# Atividade 3 - advinhaçaão com número aleatório entre 1 e 10

import random

# gera um número aleatório entre 1 e 10
num_secret = random.randint(1, 10)

# loop até o usuário acertar
while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    if palpite > num_secret:
        print("Muito alto, tente novamente!")
    elif palpite < num_secret:
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {num_secret}.")
        break # sai do loop