# Atividade 5 - Contar vogais e mostrar índices

# solicita uma frase ao usuário 
frase = input("Digite uma frase: ")

# define quais são as vogais
vogais = "aeiouAEIOU"

# lista para armazenar as vogais encontradas
vogais_enc = []

# lista para armazenar os índices das vogais
indices = []

# percorre cada letra da frase junto com seu índice
for i, letra in enumerate(frase):
    if letra in vogais:
        vogais_enc.append(letra)
        indices.append(i)

# exibe os resultados
print("Número de vogais:", len(vogais_enc))
print("Vogais encontradas:", vogais_enc)
print("Índices:", indices)