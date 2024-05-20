#atividade17.py

n = int(input("Insira um número inteiro positivo: "))

num = 0

for i in range(n):
    if i % 2 == 0:
        num = num + i
print(num)
