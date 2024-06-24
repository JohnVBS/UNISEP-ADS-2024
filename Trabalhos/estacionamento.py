#Trabalhos/estacionamento.py

carros = {}

def menu():
    try:
        # Printar o menu
        print(''' ESTACIONAMENTO!

        1 - Estacionar veículo

        2 - Retirar veículo

        3 - Veículos estacionados

        4 - Está estacionado?

        0 - Sair

        ''')
        # Input para o usuario digitar qual opcao ele vai querer
        opt = int(input('Escolha uma das opcoes: '))
        return opt
    except Exception as e:
        # Se digitar algo que nao esta no menu, printa a seguinte mensagem
        print(f'Opcao invalida: {e}')
        return 9


def estacionar():
    try:
        # Cada variavel para adicionar no dicionario carros
        placa = input('Digite a placa do veiculo: ')
        marca = input('Digite a marca do veiculo: ')
        modelo = input('Digite o modelo do veiculo: ')
        cor = input('Digite a cor do veiculo: ')
        pro = input('Digite o proprietario do veiculo: ')
        chave = {'marca': marca, 'modelo': modelo, 'cor': cor, 'proprietario': pro}
        # Dicionario carros onde a placa sera a chave para receber as informacoes do carro
        carros[placa] = chave
    except Exception as e:
        print(f'Valor invalido inserido {e}')


def retirar():
    # Input para o usuario inserir a placa do carro para retirar do estacionamento
    rem = input('Insira a placa do carro que deseja retirar: ')
    # Verificar se a placa esta no estacionamento ou nao
    if rem in carros:
        carros.pop(rem)
    else:
        # Se a placa digitada nao estiver no estacionamento, printa a seguinte mensagem
        print("Esse carro nao esta estacionado")
    input('Pressione qualquer tecla para continuar')


def listar():
    # Lista todos os carros estacionados no momento
    for placa, chave in carros.items():
        print(f"RA: {placa} - Marca: {chave['marca']} - Modelo: {chave['modelo']} - Cor: {chave['cor']} - Proprietario: {chave['proprietario']}")
    input('Pressione qualquer tecla para continuar')


def procurar():
    # Input para a procurar o carro pela placa
    placa = input('Insira a placa do carro que deseja procurar: ')
    # Se a placa inserida estiver estacionada, sera mostrada para o usuario
    if placa in carros:
        chave = carros[placa]
        print(f"Placa: {placa} - Marca: {chave['marca']} - Modelo: {chave['modelo']} - Cor: {chave['cor']} - Proprietario: {chave['proprietario']}")
    else:
        # Caso a placa nao estiver no estacionamento, printa a mensagem abaixo
        print("Esse carro nao esta estacionado")
    input('Pressione qualquer tecla para continuar')


if __name__ == '__main__':
    while True:
        # Match para executar as funcoes de acordo com a opcao escolhida na variavel opt
        match menu():
            case 1:
                estacionar()


            case 2:
                retirar()


            case 3:
                listar()


            case 4:
                procurar()


            case 0:
                break
