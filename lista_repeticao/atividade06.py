#atividade06.py

num = 0

for n in range(10):
    num = num + int(input("Insira um número inteiro: "))
    if num < 0:
        continue

num = num / 10

print(num)
