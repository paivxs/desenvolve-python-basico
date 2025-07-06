# Atividade 5 - Embaralhamento de letras interenas das palavras

import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = palavra[0] + ''.join(meio) + palavra[-1]

        nova_frase.append(palavra_embaralhada)
    else:
        nova_frase.append(palavra)

    return ' '.join(nova_frase)

# exemplo de uso
frase = "Python é uma linguagem de prgramação"
resultado = embaralhar_palavras(frase)
print(resultado)
