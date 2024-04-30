# par_impar.py

num = int(input("Insira um número para o intervalo: "))
ip = input("Pares ou ímpares? (P - I)")

print("-----------")

for n in range(num + 1):
    if n % 2 == 0:
        if ip.upper() == "P":
            print(f"O número {n} é par!")
    else:
        if ip.upper() == "I":
            print(f"O número {n} é ímpar!")
