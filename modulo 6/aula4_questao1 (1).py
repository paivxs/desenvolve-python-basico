# Exercício 1

# todos números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]
print("Números pares entre 20 e 50:", pares)

# todos os números entre 1 e 10 elevados ao quadrado 
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
quadrados = [x**2 for x in l1]
print("Quadrados de 1 a 10:", quadrados)

# todos os números divisíveis por 7
divisiveis7 = [x for x in range(1, 101) if x % 7 == 0]
print("Números entre 1 e 100 divisíveis por 7:", divisiveis7)

# para todos valores em range(0, 30, 3) encreve par ou ímpar dependendo da paridade do número
par_impar = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print("Paridade dos valores em range(0, 30, 3):", par_impar)




