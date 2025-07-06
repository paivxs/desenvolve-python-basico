# Atividade 3
# análise do roteiro do filme "Estômago"

# abre o arquivo estomago.txt para leitura
with open("estomago.txt", "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines() # lê todas as linhas como lista

# 1- mostra as primeiras 25 linhas do arquivo
print("=== Primeiras 25 linhas do arquivo ===")
for linha in linhas[:25]:
    print(linha.strip())

# 2- mostra o número total de linhas do arquivo
print("\n=== Total de linhas no arquivo ===")
print(len(linhas))

# 3- mostra a linha com o maior número de caracteres
linha_maior = max(linhas, key=len)
print("\n=== Linha com mais caracteres ===")
print(linha_maior.strip())
print(f"Quantidade de caracteres: {len(linha_maior.strip())}")

# 4- conta as menções aos personagens "Nonato" e "Íria"
# ignora maiúsculas e evita contar "Íria" dentro de outras palavras
import re

conteudo = ''.join(linhas).lower() # junta tudo e coloca em minúsculo

# conta ocorrências exatas usando regex com bordas de palavras
mencoes_nonato = len(re.findall(r'\bnonato\b', conteudo))
mencoes_iria = len(re.findall(r'\biria\b', conteudo))

print("\n=== Menções aos personagens ===")
print(f"Nonato: {mencoes_nonato} mencoes")
print(f"Íria: {mencoes_iria} mencoes")