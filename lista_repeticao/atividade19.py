#atividade19.py

num = int(input("Insira um número inteiro entre 100 e 999: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10

print(f"Os algarismos que formam esse número são o {c}, o {d} e o {u}")
