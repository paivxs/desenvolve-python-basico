# Atividade 6
# descobrir as músicas mais populares do Spotify nos últimos 10 anos

# importa a biblioteca pandas
import pandas as pd

# lê o arquivo CSV 
arquivo = 'spotify-2023.csv'

# lê o CSV com codificação correta 
dados = pd.read_csv(arquivo, encoding="latin-1")

# lê as 5 primeiras linhas
print("Primeiras linhas da tabela:")
print(dados.head())

# filtra musicas lançadas entre 2012 e 2022
dados_filtrados = dados[
    (dados['released_year'] >= 2012) &
    (dados['released_year'] <= 2022)
]

# conferi se filtrou corretamente
print("\n Dados filtrados de 2012 a 2022:")
print(dados_filtrados[['track_name', 'artist(s)_name', 'released_year', 'streams']].head())

# cria lista com a musica mais tocada de cada ano
resultado = []

for ano in range(2012, 2023):
    dados_ano = dados_filtrados[dados_filtrados['released_year'] == ano]

if not dados_ano.empty:
    top_musica = dados_ano.sort_values(by='streams', ascending=False).iloc[0]

# adiciona na lista no formato pedido
resultado.append([
    top_musica['track_name'],
    top_musica['artist(s)_name'],
    top_musica['released_year'],
    top_musica['streams']
])

# imprime o resultado
print("\nLista com as músicas mais tocadas de cada ano (2012 a 2022): ")
for item in resultado:
    print(item)

print(resultado)