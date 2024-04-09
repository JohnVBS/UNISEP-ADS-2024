# atividade11.py
import math

num = int(input("Insira um número inteiro: "))

if num<0:
    print("Número inválido")
else:
    logaritmo = math.log(num)
    print(f"O logaritmo desse número é: {logaritmo}")