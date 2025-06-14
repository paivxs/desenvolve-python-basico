# Lê a quantidade de entrevistados
N = int(input("Digite a quantidade de entrevistados: "))

# Inicializa a soma das idades e o contador
soma_idades = 0
contador = 0

# Enquanto o contador for menor que N
while contador < N:
    idade = int(input(f"digite a idade da pessoa{contador + 1}: "))
    soma_idades += idade # Soma a idade
    contador += 1 # Atualiza o contador

# Calcula a média 
media = soma_idades / N

# Imprime a média
print("Média das idades:", media)