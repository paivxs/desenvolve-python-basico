# Exercício 2 
# extrai o nome principal de cada domínio de uma lista de URL

# lista com endereço de sites
urls = ["www.google.com" , "www.gmail.com" , "www.github.com" , "www.reddit.com" , "www.yahoo.com"]

# lista por compressão (list comprehesion)
# para cada URL, split(".") para separar aonde tem ponto
# depois pega o segundo elemento [1] que é o nome principal 

dominios = [url.split(".")[1] for url in urls]

# mostra a lista final com os nomes dos domínios
print("Domínios:", dominios)
