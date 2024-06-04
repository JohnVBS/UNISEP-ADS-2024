#funcoes/medias.py

alunos = {}

def menu():
    try:
        print('''\nNOTAS
        1 - adicionar aluno
        2 - listar aluno
        3 - remover aluno
        4 - procurar aluno
        5 - aprovados
        6 - reprovados
        0 - sair''')
        opt = int(input("\nSelecione uma das opcoes: "))
        return opt
    # except KeyboardInterrupt:
    #     print('Deu pau no teclado!')
    # except ValueError:
    #     print('Numero digitado errado!')
    except Exception as e:
        print(f'Opcao invalida: {e}')
        return 9
    # finally:
    #     print('mostra isso!')

def add_aluno():
    try:
        ra = input('Digite o RA do Aluno: ')
        nome = input('Digite o nome do Aluno: ')
        nota_b1 = float(input('Digite a nota B1 do Aluno: '))
        nota_b2 = float(input('Digite a nota B2 do Aluno: '))
        dados = {"nome": nome, 'b1': nota_b1, 'b2': nota_b2}
        alunos[ra] = dados
    except Exception as e:
        print(f'Valor invalido inserido {e}')


def listar_aluno():
    for ra, dados in alunos.items:
        print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
    input('Pressione qualquer tecla para continuar')


def remover_aluno():
    rem = input('Insira o RA do Aluno que deseja remover: ')
    if rem in alunos:
        alunos.pop(rem)
    else:
        print("Esse Aluno nao esta listado")


def procurar_aluno():
    pro = input('Insira o RA do Aluno que deseja procurar: ')
    if pro in alunos:
        print("Esse Aluno esta listado")
    else:
        print("Esse Aluno nao esta listado")


def aprovados():
    

def reprovados():


if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                add_aluno()


            case 2:
                listar_aluno()


            case 3:
                remover_aluno()


            case 4:
                procurar_aluno()


            case 5:
                aprovados()


            case 6:
                reprovados()


            case 0:
                break
