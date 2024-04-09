# atividade7.py

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Agora, o segundo: "))

if num1>num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num2>num1:
    print(f"O número {num2} é maior que o número {num1}")
else:
    print("Números iguais")