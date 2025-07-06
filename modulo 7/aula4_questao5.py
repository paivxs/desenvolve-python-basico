# Atividade 5
# planilha de livros

# cria o arquivo CSV com livros 
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:

    # cabeçalho
    arquivo.write("Titulo,Autor,Ano de publicaão,Numero de páginas\n")

    # livros variados
    arquivo.write("O caçador de pipas,Khaled Hosseini,2003,368\n")
    arquivo.write("Torto arado,Itamar Vieira Junior,2019,264\n")
    arquivo.write("A menina que roubava livros,Markus Zusak,2005,480\n")
    arquivo.write("Harry Potter e a pedra filosofal,J.K. Rowling,1997,223\n")
    arquivo.write("Crepúsculo,Stephenie Meyer,2005,434\n")
    arquivo.write("O pequeno príncipe,Antoine de Saint-Exupéry,1943,96\n")
    arquivo.write("Dom Casmurro,Machado de Assis,1899,256\n")
    arquivo.write("Capitães da areia,Jorge Amado,1937,272\n")
    arquivo.write("A culpa é das estrelas,John Green,2012,313\n")
    arquivo.write("1984,George Orwell,1949,328\n")

    print("Arquivo 'Arquivo meus_livros.csv' criado com sucesso!")
