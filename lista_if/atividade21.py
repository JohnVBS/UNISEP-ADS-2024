# atividade21.py

ano = int(input("Insira um ano: "))

if ano >= 0:
    if (ano % 4 == 0) or (ano % 400 == 0) and (ano %100 != 0):
        print("Esse ano é bissexto!")
    else:
        print("Esse ano não é bissexto!")
else:
    ("Ano inválido!")