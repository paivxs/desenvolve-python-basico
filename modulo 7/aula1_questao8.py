# Atividade 7 - Verificador de CPF

def validar_cpf(cpf):
    # remove pontos e traço
    cpf = cpf.replace('.', '').replace('-','')

    # verifica se tem 11 digitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # verifica se todos os digitos são iguais
    if cpf == cpf[0] * 11:
        return "Inválido"
    
    # calculo do primeiro digito
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    # calculo segundo digito
    soma2 = 0
    for i in range(9):
        soma2 += int(cpf[i]) * (11 - i)
    soma2 += digito1 * 2
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    # compara os dois ultimos dígitos do CPF com os dígitos calculados
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return "Válido"
    else:
        return "Inválido"
    
# pede o CPF ao usuário
cpf_usuario = input("Digite um CPF: ")
print(validar_cpf(cpf_usuario))