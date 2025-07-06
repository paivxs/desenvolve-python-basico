# Atividade 6 - Encontrar anagramas

import string
def limpar_palavra(palavra):
    return palavra.strip(string.punctuation).lower()

# solicita uma frase e a palavra objetivo
frase = input("Digite uma frase: ")
palavra_alvo = input("Digite a palavra objetivo: ")

# limpa e organiza a palavra alvo
palavra_ordenada = sorted(limpar_palavra(palavra_alvo))

# divide a frase em palavras e cria lista de anagramas
palavras = frase.split()
anagramas = []

# verifica se cada palavra da frase é anagrama
for p in palavras:
    if sorted(limpar_palavra(p)) == palavra_ordenada:
        anagramas.append(p)

# mostra os anagramas encontrados
print("Anagramas encontrados:", anagramas)