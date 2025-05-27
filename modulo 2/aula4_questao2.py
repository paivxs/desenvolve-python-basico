#Na opção abaixo, solicitamos o valor a ser convertido para o usuario (entrada)
F = float(input("Digite a temperatura em Farharenheit: "))

#Na expressão abaixo, ocorre a conversão (Processamento)
C = (F-32)*5/9

#Imprimimos os dados
print(f"{F} grau Fahrenheit são {int(C)} graus Celsius.")