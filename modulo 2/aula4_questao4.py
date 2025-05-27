valor = int(input("Escreva um valor inteiro: "))

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor %50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas2 = valor // 2
valor = valor % 2

notas1 = valor // 1
valor = valor % 1

print (f"{notas100} nota(s) de 100")
print (f"{notas50} nota(s) de 50")
print (f"{notas20} nota(s) de 20")
print (f"{notas10} nota(s) de 10")
print (f"{notas5} nota(s) de 5")
print (f"{notas2} nota(s) de 2")
print (f"{notas1} nota(s) de 1")