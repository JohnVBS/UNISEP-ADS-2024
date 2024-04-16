# atividade18.py

num = int(input("Insira um número inteiro: "))

if num >= 0:
    if (num % 3 == 0) ^ (num % 5 == 0):
        print("\nO número é divisível por 3 ou por 5, mas não pelos dois!")
else:
    print("Número inválido!")