# Lê a quantidade de experimentos 
N = int(input("Digite o número de registros de cobaias: "))

# Inicializa os contadores
total = 0
coelhos = 0
ratos = 0
sapos = 0

# Inicializa contador de controle
i = 0

# Loop while para ler os dados
while i < N:
    entrada = input("Digite a quantidade e o tipo de cobaia: ").split()
    quantidade = int(entrada[0])
    tipo = entrada[1].upper() # Converte para maiúsculo para evitar erros

    total += quantidade
    if tipo == 'C':
        coelhos += quantidade
    elif tipo == 'R':
        ratos += quantidade
    elif tipo == 'S':
        sapos += quantidade

    i += 1

# Calcula os percentuais
perc_coelhos = (coelhos / total) * 100
perc_ratos = (ratos / total) * 100
perc_sapos = (sapos / total) * 100

#Exibe os resultados
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f}%")
print(f"Percentual de ratos: {perc_ratos:.2f}%")
print(f"Percentual de sapos: {perc_sapos:.2f}%")