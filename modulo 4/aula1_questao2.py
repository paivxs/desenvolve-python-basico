# Lê um número digitado e armazena na variável n
n = int(input("Digite um número: "))

# Inicializa o contador com 0
cont = 0

# Enquanto o valor de cont for menor que n, repete o bloco
while cont < n:
    # Soma 1 ao contador
    cont = cont + 1
    # Imprime o valor atual do contador
    print(cont)

# Quando o laço termina, imprime "Fim"
print("Fim")