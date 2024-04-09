# atividade6.py

num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Agora, o segundo número inteiro: "))

if num1>num2:
    dif = num1-num2
    print(f'''O número {num1} é maior que o número {num2}
E sua diferença é {dif}''')
else:
    dif = num2-num1
    print(f'''O número {num2} é maior que o número {num1}
E sua diferença é {dif}''')