# Atividade 2 - Substituição de vogais por asteriscos
 # solicita a frase
frase = input("Digite uma frase: ")

# define as vogais
vogais = "aeiouAEIOU"

# substitui cada vogal por "*"
frase_mod = ""
for letra in frase:
    if letra in vogais:
      frase_mod += "*"
    else:
     frase_mod += letra

# imprime o resultado
print("Frase modificada:,", frase_mod)