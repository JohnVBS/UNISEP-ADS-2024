#atividade06.py

num = 0
num2 = num

for n in range(10):
    num = num + float(input("Insira um número inteiro: "))
    if num < 0:
        continue
print(num)