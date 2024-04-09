# atividade3.py
import math

num = float(input("Insira um número real: "))

if num>=0:
    raiz = math.sqrt(num)
    print(f"A raiz quadrada desse número é: {raiz}")

else:
    qua = num*num
    print(f"O valor desse número ao quadrado é: {qua}")
