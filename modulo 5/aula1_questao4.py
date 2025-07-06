# Atividade 4 - Exibe a data e hora atuais formatadas

import datetime

# pega a data e hora atual
agora = datetime.datetime.now()

# formata e exibe a data
print(f"Data: {agora.day:02}/{agora.month:02}/{agora.year}")

# formata e exibe a hora
print(f"Hora: {agora.hour:02}:{agora.minute:02}")