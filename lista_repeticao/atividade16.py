#atividade16.py

num = int(input("Insira um número inteiro PAR: "))

lista = []

for i in range (num + 1):
    if i % 2 != 0:
        lista.append(i)
lista.reverse()
print(lista)
