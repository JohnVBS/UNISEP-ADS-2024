# atividade20.py

idade = int(input("Insira a idade do trabalhador: "))
tempo = float(input("Agora, o tempo de serviço em anos: "))

if idade >=0 and tempo >=0:
    if (idade >= 65) or (tempo >= 30) or (idade >=60 and tempo >= 25):
        print("O trabalhador pode se aposentar!")
    else:
        print("O trabalhador NÃO pode se aposentar ainda!")
else:
    print("idade ou tempo de serviço inválidos!")