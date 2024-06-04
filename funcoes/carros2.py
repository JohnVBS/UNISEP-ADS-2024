#funcoes/carros2.py

carros = {
    "AAA-0001": ("JJJJJ", 1599.00),
}

print(carros)

def menu():
    print('''\nCARROS
    1 - Adicionar
    2 - Remover                          
    3 - Listar             
    4 - Verificar se está na lista             
    0 - Sair             
    ''')
    opt = input("Selecione uma das opcoes: ")
    

def add():
    placa = input("Digite a placa: ")
    modelo = input("Modelo: ")
    valor = float(input("Valor: "))
    carros[placa] = (modelo, valor)


def remover():
    rem = input("Qual carro voce gostaria de remover da lista? ")
    if rem in carros:
        carros.remove(rem)
    else:
        print("Esse carro nao esta na lista!")


def listar():
    print(carros)


def buscar():
    


def caminho(opt):
    match opt:
        case '1':
            add()
        case '2':
            remover()
        case '3':
            listar()
        case '4':
            buscar()
        case '0':
            return False
    return True

def main():
    while True:
        opt = menu()
        if not caminho(opt):
            break

if __name__ == '__main__':
    main()
