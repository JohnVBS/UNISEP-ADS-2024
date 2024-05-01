# atividade3.py

notas = []

for n in range(10):
    notas.append(float(input("Insira a nota do aluno: ")))
    notas.sort()

print(f"A maior nota é {notas[9]}! E a menor é {notas[0]}!")
