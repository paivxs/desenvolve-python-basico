# Exercício 3

# lista com as horas trabalhadas por cada funcionário
horas_trabalhadas = [40, 37, 45, 40, 40, 48]

# valor pago por hora de trabalho
valor_hora = 20

# valor hora extra
hora_extra = 25

# lista de pagamentos calculada com compreensão de listas
# se trabalhou ate 40h paga normal, se passou de 40h calcula horas extras 
pagamentos = [valor_hora * min(hora, 40) + \
              hora_extra * max(0, hora-40)
              for hora in horas_trabalhadas]

# mostra o resultado
print("Pagamentos:", pagamentos)
