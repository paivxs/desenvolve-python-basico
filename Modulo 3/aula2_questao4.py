# Atividade 4

# Solicita dados dos personagens
classe = input("Escolha uma classe (guerreiro,mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verifica se os atributos são validos para a classe escolhida
if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = magia >= 15 and forca <= 10
elif classe == "arqueiro":
    valido = forca >= 12 and magia >= 12 
else:
    valido = False 

# Resultado (saída)
print("Pontos de atributo consistentes com a classe escolhida:", valido)