# atividade14.py

num = int(input("Insira um número inteiro entre 1 e 7: "))

if num >=1 and num <=7:
    match num:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")
        case 7:
            print("Sábado")
else:
    print("Um ou mais números inválidos")
