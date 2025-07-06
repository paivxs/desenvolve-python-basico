# Exercício 2 

# solicita ao usuário que digite um frase
frase = input("Digite uma frase: ")

# lista das vogais da frase, ordenada alfabeticamente
vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])
print("Vogais da frase:", vogais)

# lista das consoantes, somente letra (sem espaços ou pontuação)
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in'aeiou']
print("Consoantes da frase:", consoantes)