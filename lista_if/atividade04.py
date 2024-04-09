# atividade4.py
import math

num = float(input("Insira um número: "))

if num>=0:
    qua = num*num
    raiz = math.sqrt(num)
    print(f'''
Esse número ao quadrado é {qua}
A raiz desse número é {raiz}
''')
else:
    print("Número inválido")
