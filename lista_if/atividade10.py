# atividade10.py

num = int(input("Insira um número inteiro maior do que 0: "))
soma = 0

if num > 0:
    while (num > 0):
        resto = num % 10
        num = (num - resto)/10
        soma = soma + resto
    print(f"A soma doa algarismos desse número é: {soma}")
else:
    print("Número inválido")