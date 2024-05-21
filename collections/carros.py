#collections/carros.py

carros = []

while True:
    menu = int(input('''\nCARROS
    1 - Adicionar
    2 - Remover                          
    3 - Listar             
    4 - Verificar se está na lista             
    0 - Sair             
    '''))

    match(menu):
        case 1:
            print("\nVocê escolheu ADICIONAR!\n")

            add = input("Adicione o nome de um carro: ")

            if add in carros:
                print("\nESTE CARRO JA ESTA NA LISTA!")
                continue
            else:
                carros.append(add)
                print("\nCarro adicionado com sucesso!")


        case 2:
            print("\nVoce escolheu REMOVER!\n")

            rem = input("Remova o nome de um carro: ")

            if rem in carros:
                carros.remove(rem)
                print("\nCarro removido com sucesso!")
            else:
                print("\nESTE CARRO NAO ESTA NA LISTA!")


        case 3:
            print("\nVoce escolheu LISTAR!\n")

            print(carros)


        case 4:
            print("\nVoce escolheu VERIFICAR!\n")

            ver = input("Insira o nome de um carro para verificar se esta na lista: ")

            if ver in carros:
                print("\nESTE CARRO JA ESTA NA LISTA!")
            else:
                print("\nESTE CARRO NAO ESTA NA LISTA!")


        case 0:
            break
