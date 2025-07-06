# Atividade 3 - Verificação de Palíndromos com repetição até o fim

import string

while True:
    frase = input("Digite uma frase (fim para encerrar): ")

    if frase.lower() == "fim":
        break

    # remove espaços, pontuação e deixa tudo minúsculo
    frase_limpa = frase.lower()
    frase_limpa = ''.join(c for c in frase_limpa if c.isalnum())

    # verifica se é palíndromo
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é Palíndromo.')

    else:
        print(f'"{frase}" não é Palíndromo.')