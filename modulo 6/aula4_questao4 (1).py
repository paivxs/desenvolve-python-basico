# exercício 4

# lista com nomes dos alunos
alunos = ['João', 'Ana', 'Carlos', 'Sol']

# lista com as notas dos alunos na mesma ordem
notas = [35, 50, 20, 80]

# lista de aprovados (nota maior ou igual a 50) usando compreensão de listas
# a condição é aplicada sobre os índices das listas
aprovados = [alunos[i] for i in range(len(alunos)) if notas[i] >= 60]

# mostra os alunos aprovados
print("Alunos aprovados:", aprovados)
