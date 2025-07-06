# Atividade 2
# lê a frase do arquivo, limpa os caracteres e salva palavras separadas

# abre o arquivo "frase.txt" e lê o conteúdo
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    frase = arquivo.read()

# remove os caracteres que não são letras ou espaços
import re
palavras = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚçÇêôãõâÂÊÔÃÕ] + \b', frase)

# salva cada palavra em uma nova linha no arquivo "palavras.txt"
with open("palavras.txt", "w", encoding="utf-8") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")

# mostra o conteúdo do arquivo "palavras.txt"
with open("palavras.txt", "r", encoding="utf-8") as arquivo_palavras:
    print(arquivo_palavras.read())