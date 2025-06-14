# Questão 1

# Entrada de dados 
# Lê os números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Processamento (Calcula a soma)
soma = num1 + num2

# verifica se a soma é ímpar ou par
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")