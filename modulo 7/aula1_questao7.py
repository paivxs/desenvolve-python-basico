# Atividade 7 - Criptografia simples

import random

# função para criptografar
def encrypt(lista_nomes):
    chave = random.randint(1, 10) # gera chave aleatoria entre 1 a 10
    criptografados = [] # lista para guardar os nomes criptografados

    for nome in lista_nomes:
        novo_nome = ""
        for letra in nome:
            novo_nome += chr(ord(letra) + chave)
# coverte letra para unicode, aplica chave e volta para carctere
        criptografados.append(novo_nome)
    return criptografados, chave 
# retorna os nomes criptografados e a chave

# lista de nomes de exemplo
nomes = ["Franciele", "Ju", "Davi", "Vivi", "Gabriela"]

# usa a função e mostra o resultado
nomes_cript, chave_usada = encrypt(nomes)
print("Nomes criptografados:", nomes_cript)
print("Chave utilizada:", chave_usada)