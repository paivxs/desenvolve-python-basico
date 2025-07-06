# Atividade 5 - Sistema de mensagens com emojis 

import emoji

emojis_disponiveis = {
    ":red_heart:": "❤",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
 }

# mostraa os emojis disponíveis pro usuário
print("Emojis disponíveis:")
for codigo, simbolo in emojis_disponiveis.items():
    print(f"{simbolo} - {codigo}")

# pede a frase para o usuário
frase = input("\nDigite uma frase e ela será emojizada:\n")

# converte a frase usando a função emotize 
frase_emojis = emoji.emojize(frase)

# exibe o resultado
print("\nFrase emojizada:")
print(frase_emojis)
