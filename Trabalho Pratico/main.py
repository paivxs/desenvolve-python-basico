# Trabalho prático - Sistema FranSoft
# Sistema de gerenciamento de usuários e produtos

import os

# ====================================
# Funções de arquivo
# ====================================

def carregar_usuario():
    # carrega os usuários do arquivo usuarios.txt, se existir
    usuarios = []
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as f:
            for linha in f:
                nome, senha, tipo = linha.strip().split(",")
                usuarios.append({"nome": nome, "senha": senha, "tipo": tipo})
    return usuarios

def salvar_usuarios(usuarios):
    # salva os usuarios do arquivo usuarios.txt
    with open("usuarios.txt", "w") as f:
        for u in usuarios:
            f.write(f"{u['nome']}, {u['senha']}, {u['tipo']}\n")

def carregar_produtos():
    # carrega os produtos do arquivo produtos.txt, se existir
    produtos = []
    if os.path.exists("produtos.txt"):
        with open("produtos.txt", "r") as f:
            for linha in f:
                nome, preco, qtd = linha.strip().split(",")
                produtos.append({"nome": nome, "preco": float(preco), "qtd": int(qtd)})
    return produtos

def salvar_produtos(produtos):
    # salva os produtos no arquivo produtos.txt
    with open("produtos.txt", "w") as f:
        for p in produtos:
            f.write(f"{p['nome']}, {p['preco']}, {p['qtd']}\n")

# ====================================
# CRUD de uruários
# ====================================

def cadastrar_usuario(usuarios):
    # cadastra um novo usuario
    nome = input("Novo nome de usuário: ")
    senha = input("Senha: ")
    tipo = input("Tipo (admin/comum): ")
    usuarios.append({"nome": nome, "senha": senha, "tipo": tipo})
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!\n")

def listar_usuarios(usuarios):
    # lista todos os usuarios cadastrados
    print("---Lista de usuários---")
    for u in usuarios:
        print(f"Nome:{u['nome']}, Tipo:{u['tipo']}") 
    print()

def atualizar_usuario(usuarios):
    # atualiza a senha de um usuario existente
    nome = input("Nome do usuário a atualizar: ")
    for u in usuarios:
        if u["nome"] == nome:
            nova_senha = input("Nova senha: ")
            u["senha"] = nova_senha
            salvar_usuarios(usuarios)
            print("Senha atualizada com sucesso!\n")
            return
        print("Usuário não encontrado.\n")

def deletar_usuario(usuarios):
    # deleta um usuario da lista
    nome = input("Nome do usuário a deletar: ")
    for u in usuarios:
        if u["nome"] == nome:
            usuarios.remove(u)
            salvar_usuarios(usuarios)
            print("Usuário removido com sucesso.\n")
            return
    print("Usuário não encontrado.\n")

# ====================================
# CRUD produtos
# ====================================

def cadastrar_produto(produtos):
    # cadastra um novo produto
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade: "))
    produtos.append({"nome": nome, "preco": preco, "qtd": qtd})
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!\n")

def listar_produtos(produtos):
    # lista todos os produtos cadastrados
    print("---Lista de produtos---")
    for p in produtos:
        print(f"Nome: {p['nome']}, Preço: R${p['preco']:.2f}, Quantidade: {p['qtd']}")
    print()

def buscar_produto(produtos):
    # busca um produto pelo nome (ignora maiusculas/minusculas)
    nome = input("Digite o nome do produto para buscar: ")
    encontrado = False
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            print(f"Encontrado: Nome: {p['nome']}, Preço: R${p['preco']:.2f}, Quantidade: {p['qtd']}\n")
            encontrado = True
            break
    if not encontrado:
     print("Produto não encontrado.\n")

def ordenar_produtos(produtos):
    # ordena a lista de produtos por nome ou preço
    print("1. Ordenar por nome\n2. Ordenar por preço")
    op = input("Escolha uma opção: ")
    if op == "1":
        ordenado = sorted(produtos, key=lambda x: x["nome"])
    else:
        ordenado = sorted(produtos, key=lambda x: x["preco"])
    listar_produtos(ordenado)

def atualizar_produto(produtos):
    # atualiza o preço e quantidade de um produto
    nome = input("Digite o nome do produto a atualizar: ")
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            p["preco"] = float(input("Novo preço: "))
            p["qtd"] = float(input("Nova quantidade: "))
            salvar_produtos(produtos)
            print("Produto atualizado com sucesso!\n")
            return
    print("Produto não encontrado.\n")

def deletar_produto(produtos):
    # deleta um produto pelo nome
    nome = input("Digite o nome do produto a deletar: ")
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            produtos.remove(p)
            salvar_produtos(produtos)
            print("Produto deletado com sucesso!\n")
            return
    print("Produto não encontrado.\n")

# ==================================== 
# Sistema principal - login e menus
# ====================================

def login(usuarios):
    # realiza o login validando nome e senha
    nome = input("Usuário: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u["nome"] == nome and u ["senha"] == senha:
            print(f"\nBem-vindo(a), {nome}! Tipo de conta: {u['tipo']}\n")
            return u
    print("Login inválido.\n")
    return None

def menu_admin(usuarios, produtos):
    # menu com opção de admin(gerencia usuarios e produtos)
    while True:
        print("1. CRUD usuários")
        print("2. CRUD produtos")
        print("3. CRUD logout")
        opc = input("Escolha: ")
        if opc == "1":
            print("1. Cadastrar usuário\n2. Listar\n3. Atualizar\n4. Deletar")
            acao = input("Opção: ")
            if acao == "1": cadastrar_usuario(usuarios)
            elif acao == "2": listar_usuarios(usuarios)
            elif acao == "3": atualizar_usuario(usuarios)
            elif acao == "4": deletar_usuario(usuarios)
        elif opc == "2":
            print("1. Cadastrar produto\n2. Listar\n3. Buscar\n4. Ordenar\n5. Atualizar\n6. Deletar")
            acao = input("Opção: ")
            if acao == "1": cadastrar_produto(produtos)
            elif acao == "2": listar_produtos(produtos)
            elif acao == "3": buscar_produto(produtos)
            elif acao == "4": ordenar_produtos(produtos)
            elif acao == "5": atualizar_produto(produtos)
            elif acao == "6": deletar_produto(produtos)
        elif opc == "3": break
        else: print("Opção inválida.\n")

def menu_comum(produtos):
    # menu com opções para usuário comum (vizualização de produtos)
    while True:
        print("1. Listar produtos\n2. Buscar\n3. Ordenar\n4. logout")
        opc = input("Escolha: ")
        if opc == "1": listar_produtos(produtos)
        elif opc == "2": buscar_produto(produtos)
        elif opc == "3": ordenar_produtos(produtos)
        elif opc == "4": break
        else: print("Opção inválida.")

def main():
    # função principal que inicia o sistema
    usuarios = carregar_usuario()
    produtos = carregar_produtos()

    while True:
        print("--- Sistema FranSoft ---")
        print("1. Login\n2. Sair")
        opc = input("Escolha: ")
        if opc == "1": 
            user = login(usuarios)
            if user:
                if user["tipo"] == "admin":
                    menu_admin(usuarios, produtos)
                else:
                    menu_comum(produtos)
        elif opc == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    main()
