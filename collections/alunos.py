#collections/alunos.py

alunos = []

while True:
    nome = input("Insira o nome do aluno: ")
    if (nome == ''):
        break
    alunos.append(nome)

print(alunos)
for aluno in alunos:
    print(f"Aluno: {aluno}")
