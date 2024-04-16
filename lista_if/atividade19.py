# atividade19.py

print("Digite os valores de cala lado de um TRIÂNGULO\n")
num1 = float(input("Insira o valor de A: "))
num2 = float(input("Insira o valor de B: "))
num3 = float(input("Insira o valor de C: "))

if (num1 >= 0) and (num2 >= 0) and (num3 >= 0):
    if (num1 < num2+num3) and (num2 < num1+num3) and (num3 < num1+num2):
        if num1 == num2 == num3:
            print("\nO triângulo é equilátero")
        elif (num1 == num2 > num3) or (num1 == num3 > num2) or (num2 == num3 > num1):
            print("\nO triângulo é isósceles")
        elif num1 != num2 != num3:
            print("\nO triângulo é escaleno")
    else:
        print('''Esses valores não servem para um triângulo!
              
Para ser um triângulo, cada lado PRECISA ser
menor que a soma dos outros 2 lados''')
else:
    ("Um ou mais números inválidos!")