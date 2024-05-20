#atividade07.py

num = []

for n in range(10):
    n =  float(input("Insira um número inteiro: "))
    num.append(n)
num.sort()

print(num[0], num[9])