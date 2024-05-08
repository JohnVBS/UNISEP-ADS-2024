# calculadora.py
while True:
    print("Calculadora HP!\n")
    opcao = input('''Selecione uma das opções:
    [ 1 ] Adição
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão
    [ X ] Sair
    ''')

    if opcao.upper() == "X":
        break

    match opcao:
        case "1":
            while True:
                print("\nVocê escolheu ADIÇÃO! Se quiser finalizar o cálculo e retornar ao menu, digite P.\n")
                c = float(input("Digite o número para calcular: "))
                match c:
                    case "P":
                        continue
                    case _:
                        cal = []
                        cal.append(c)
        case "2":
            print("2")
        case "3":
            print("3")
        case "4":
            print("4")
