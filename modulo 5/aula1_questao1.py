# Atividade 1 - calcula a diferença absoluta entre dois números decimais

# pede os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# calcula a diferença absoluta (sempre positiva)
diferenca = abs(num1 - num2)

# arredonda a diferença para duas casas decimais
diferenca = round(diferenca, 2)

# exibe o resultado
print(f"A diferença absoluta entre os números é: {diferenca}")