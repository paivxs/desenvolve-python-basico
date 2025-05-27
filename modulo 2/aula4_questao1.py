#Este comando solicita ao usuario a inserção do valor comprimento#
comprimento = int (input("Digite o comprimento: "))
#Este comando solicita ao usuario a inserção do valor largura#
largura = int(input("Digite a largura: "))
#Este comando solicita ao usuario a inserção do valor preco,com dados "quebrados"#
preco_m2 = float(input("Valor do m2: "))

area = comprimento * largura 
preco_total = area * preco_m2

print(f"O terreno possui {area}m2 e custa R${preco_total: ,.2f}")