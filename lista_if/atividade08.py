# atividade8.py

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

if (nota1 >= 0.0 and nota1 <= 10.0) and (nota2 >= 0.0 and nota2 <= 10.0):
    med = (nota1 + nota2) // 2
    print(f"A média dessas notas é: {med}")
else:
    print("Uma ou mais notas são inválidas")