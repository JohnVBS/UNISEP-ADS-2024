# atividade23.py

idade = int(input("Insira a idade do atleta: "))

if idade <5:
    print("\nNão tem idade suficiente!")
elif idade >= 5 and idade <= 7:
    print("\nInfantil A")
elif idade >= 8 and idade <= 10:
    print("\nInfantil B")
elif idade >= 11 and idade <= 13:
    print("\nJuvenil A")
elif idade >= 14 and idade <= 17:
    print("\nJuvenil B")
else:
    print("\nSenior")
