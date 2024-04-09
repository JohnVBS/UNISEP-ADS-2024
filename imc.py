# imc.py

nome = str(input("Digite o nome do funcionário: "))
altura = float(input("Digite a altura em centímetros: "))
peso = float(input("Digite o peso em quilos: "))

imc = peso / ((altura/100)*(altura/100))

if imc <= 18.5:
    print(f"{nome} está abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print(f"{nome} está no peso ideal (Para Bens)")
elif imc >= 25.0 and imc <= 29.9:
    print(f"{nome} tem sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
    print(f"{nome} tem obesidade Grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print(f"{nome} tem obesidade Grau 2")
else:
    print(f"{nome} tem obesidade Grau 3")
