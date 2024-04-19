# atividade24.py

hpar = int(input("Insira a hora de partida: "))
mpar = int(input("Insira os minutos de partida: "))
hsai = int(input("Insira a hora de saída: "))
msai = int(input("Insira os minutos de saída: "))

if hpar >= 0 and mpar >= 0 and hsai >= 0 and msai >= 0:
    if hpar > hsai:
        hfin = hsai + 24 - hpar
    else:
        hfin = hsai - hpar

    if mpar > msai:
        mfin = msai + 60 - mpar
    else:
        mfin = msai - mpar

    temp = hfin * 60 + mfin
    
    if temp <= 60:
        print("A taxa a ser para é de R$ 1,00")
    elif temp >= 61 and temp <= 120:
        print("A taxa a ser para é de R$ 2,00")
    elif temp >= 121 and temp <= 180:
        print("A taxa a ser para é de R$ 4,20")
    elif temp >= 181 and temp <= 240:
        print("A taxa a ser para é de R$ 5,60")
    else:
        fin = hfin * 2
        print(f"A taxa a ser para é de R${fin}")
else:
    print("Número inválido!")