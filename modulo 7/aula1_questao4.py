# Atividade 4 - Formatar número de celular

# solicita ao usuário o número sem traços
num = input("Digite o número: ")

# verifica se o número tem apenas 8 dígitos
if len(num) == 8:
    num = '9' + num

# formata com hifen depois do quinto dígito
num_formatado = num[:5] + '-' + num[5:]

# exibe o número formatado
print("Número completo:", num_formatado)