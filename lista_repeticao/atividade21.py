#atividade21.py

num1 = int(input("Insira um número inteiro: "))
num2 = int(input("Insira outro número inteiro: "))
soma = num1

for n in range(num1 + 1, num2 + 1):
    if n % 2 == 0:
        soma = soma + n
print(soma)
soma = num1
for n in range(num1 + 1, num2 + 1):
    if n % 2 != 0:
        soma = soma * n
print(soma)
