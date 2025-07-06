# Atividade 1 
# solicita uma frase ao usuário e salva o arquivo "frase.txt"

# solicita a frase
frase = input("Digite uma frase: ")

# cria e salva a frase no arquivo "frase.txt"
with open("frase.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# mostra o caminho do arquivo salvo
import os
caminho = os.path.abspath("frase.txt")
print("Frase salva em", caminho)

