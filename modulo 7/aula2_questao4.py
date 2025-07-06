# Atividade 4 - Validação de senha com critérios de segurança

def validador_senha(senha):
    especiais = "@#$%&*!"

    # verifica se tem pelo menos 8 caracteres
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(c in especiais for c in senha)

    # retorna true se atender a todos os critérios
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))