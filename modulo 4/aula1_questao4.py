# Lê a quantidade de números que o uruário vai digitar
n = int(input("Digite a quantidade de números: "))

# Inicializa a variável que vai guardar o maior valor
maior = 0

# Enquanto ainda houver números para ler
while n > 0:
    # Lê um número
    x = int(input("Digite um número: "))

    # Verifica se o número atual é maior do que o valor armazenado em "maior"
    if x > maior:
        maior = x # Atualiza o maior número

    # Diminui 1 da quantidade de números restantes
    n = n - 1

# Após o laço, imprime o maior valor digitado
print("Maior número digitado:", maior)