# Atividade 4 - Jogo da forca
import random

# lê as palavras do arquivo
with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip() for linha in arquivo.readlines()]

# lê os estágios do enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
    estagios = arquivo.read().split("\n\n") 

# imprime o enforcado de acordo com os erros
def imprime_enforcado(erros):
    print(estagios[erros])

# escolhe uma palavra aleatória
palavra = random.choice(palavras)
letras_descobertas = ["_" for _ in palavra]
erros = 0
letras_erradas = []

# jogo começa
print(f"A palavra tem {len(palavra)} letras: {'.'.join(letras_descobertas)}")

while erros < 6 and "_" in letras_descobertas:
    tentativa = input("Digite uma letra: ").lower()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra válida.")
        continue
    if tentativa in letras_descobertas or tentativa in letras_erradas:
         print("Você já tentou essa letra.")
         continue
    if tentativa in palavra:
        for i, letra in enumerate(palavra):
            if letra == tentativa:
                letras_descobertas[i] = letra
        print("Acertou!")
    else:
        erros += 1 
        letras_erradas.append(tentativa)
        print("Errou!") 
        imprime_enforcado(erros)

    print(" ".join(letras_descobertas))
    print(f"Erros: {erros}  | Letras erradas: {','.join(letras_erradas)}\n")

    # resultado final
    if "_" not in letras_descobertas:
        print(f"Parabéns voê vendeu!")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")
        imprime_enforcado(erros)