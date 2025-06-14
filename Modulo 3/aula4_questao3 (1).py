# Questão 3

# Pede ao usuário para digitar um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto usando as regras
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto") # Se for bissexto imprime isso
else:
    print("Não é bissexto") # Se não for bissexto imprime isso