# Questão 4

# Pede ao usuário a distância da entrega
distancia = float(input("Digite a distância da entrega em km: "))

# Pede ao usuário o peso do pacote
peso = float(input("Digite o peso do pacote em kg: "))

# Define o valor por kg conforme a distância 
if distancia <= 100:
    preco_por_kg = 1.0 #Até 100 km
elif distancia <= 300:
    preco_por_kg = 1.5 #Entre 101 e 300 km
else:
    preco_por_kg = 2.0 #Acima de 300 km

# Calcula o valor do frete
frete = peso * preco_por_kg

# Se o peso for maior que 10 kg, adiciona uma taxa extra de R$10
if peso > 10:
   frete += 10.0

# Mostra o valor total do frete com 2 casas decimais
print(f"O valor do frete é: R${frete:.2f}")
