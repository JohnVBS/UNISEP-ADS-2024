#collections/carros.py

carros = []

menu = input('''CARROS
1 - Adicionar
2 - Remover                          
3 - Listar             
4 - Verificar se está na lista             
0 - Sair             
             ''')

match(menu):
    case 1:
        print("\nVocê escolheu ADICIONAR!\n")
        add = input("Adicione o nome de um carro: ")
    case 2:

    case 3:

    case 4:

    case 0:
