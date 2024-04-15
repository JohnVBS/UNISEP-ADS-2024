# atividade17.py

print('''
============== OPERAÇÕES ==============
      
Aqui estão algumas operacões matemáticas:
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
    ''')


escolha = int(input("Agora, digite o número correspondente a operação que deseja fazer: "))

if escolha >=1 and escolha <=4:
    match escolha:
        case 1:
            print("Você escolheu ADIÇÃO")
            num1 = float(input("Digite um número: "))
            num2 = float(input("Agora, o segundo número: "))
            if num1 >=0 and num2>=0:
                add = num1 + num2
                print(f"A soma desses números é: {add}")
            else:
                print("Um ou mais números inválidos")
        case 2:
            print("Você escolheu SUBTRAÇÃO")
            num1 = float(input("Digite um número: "))
            num2 = float(input("Agora, o segundo número: "))
            if num1 >=0 and num2>=0:
                sub = num1 - num2
                print(f"A diferença desses números é: {sub}")
            else:
                print("Um ou mais números inválidos")
        case 3:
            print("Você escolheu MULTIPLICAÇÃO")
            num1 = float(input("Digite um número: "))
            num2 = float(input("Agora, o segundo número: "))
            if num1 >=0 and num2>=0:
                mult = num1 * num2
                print(f"A multiplicação desses números é: {mult}")
            else:
                print("Um ou mais números inválidos")
        case 4:
            print("Você escolheu DIVISÃO")
            num1 = float(input("Digite um número: "))
            num2 = float(input("Agora, o segundo número: "))
            if num1 >=0 and num2>=0:
                div = num1 // num2
                print(f"A divisão desses números é: {div}")
            else:
                print("Um ou mais números inválidos")
else:
    print("Número inválido")