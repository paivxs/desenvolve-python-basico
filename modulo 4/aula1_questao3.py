# Lê 3 notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Calcula a média das 3 notas
m = (n1 + n2 + n3) / 3

# Verifica a média e imprime o resultado conforme a condição
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

# Imprime "Fim" ao final do programa
print("Fim")