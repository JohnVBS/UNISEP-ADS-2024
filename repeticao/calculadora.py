# calculadora.py

while True:    # "while" para toda vez que terminar um cálculo, o programa volta para o início.
    cal = 0    # Variáveis zeradas para que toda vez que terminar um cálculo, elas voltem a ter o valor zero para não ter problema nos cálculos.
    flag = 0

    print("Calculadora HP!\n")     # "print" para imprimir o que esta entre parênteses na tela. "\n" para quebra de linhas.

    opcao = input('''Selecione uma das opções:
    [ 1 ] Adição
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão
    [ X ] Sair
    ''')    # Input para armazenar na variável "opcao", o valor inserido pelo usuário.

    if opcao.upper() == "X":    # "upper" para se o usuário inserir a letra "x" em minúsculo, ela se torna maiúscula.
        break    # "break" para se a condição "if" for VERDADEIRA, o laço acaba. Assim, terminando o programa.

    match opcao:    # "match" para cada opção da variável "opcao". Se o usuário escolher uma das opções dessa variável, as outras não serão utilizadas.
        case "1":    # Nomear cada "case" para cada opção.
            while True:    # "while" para repetir as funções dentro dele, até que seja FALSO.
                print("\nVocê escolheu ADIÇÃO! Se quiser finalizar o cálculo e retornar ao menu, digite P.\n")     # "print" para imprimir o que esta entre parênteses na tela.

                c = input("Digite o número para calcular: ")    # Input para armazenar na variável "c", o valor inserido pelo usuário.

                if flag == 0:    # "flag" já é zero. Então, a primeira vez que chegar nesse "if", será VERDADEIRO. 
                    cal = float(c)     # Variável que irá copiar o valor de "c" transformado em "float", para que possa ser utilizado para cálculo.
                    flag = flag + 1    # "flag" aumentará 1 valor para que quando esse laço se repetir, a condição "if" seja FALSA.
                else:   # "else" para que quando "if" for FALSO, o programa entra aqui e executa suas funções.
                    if c.upper() != "P":    # "upper" para se o usuário inserir a letra "p" em minúsculo, ela se torna maiúscula.
                        cal = cal + float(c)    # "cal" já terá seu valor modificado pelo input da variável "c", então ele irá somar com o próximo valor de "c" e substituirá o resultado na mesma variável "cal".
                    else:    # "else" para que quando "if" for FALSO, o programa entra aqui e executa suas funções.
                        print(cal)    # Imprime o resultado final do cálculo armazenado na variável "cal".
                        break    # Interrompe o laço e volta para o início do programa.


        case "2":
            while True:
                print("\nVocê escolheu SUBTRAÇÃO! Se quiser finalizar o cálculo e retornar ao menu, digite P.\n")

                c = input("Digite o número para calcular: ")

                if flag == 0:    
                    cal = float(c)
                    flag = flag + 1
                else:
                    if c.upper() != "P":
                        cal = cal - float(c)
                    else:
                        print(cal)
                        break


        case "3":
            while True:
                print("\nVocê escolheu MULTIPLICAÇÃO! Se quiser finalizar o cálculo e retornar ao menu, digite P.\n")

                c = input("Digite o número para calcular: ")

                if flag == 0:    
                    cal = float(c)
                    flag = flag + 1
                else:
                    if c.upper() != "P":
                        cal = cal * float(c)
                    else:
                        print(cal)
                        break


        case "4":
            while True:
                print("\nVocê escolheu DIVISÃO! Se quiser finalizar o cálculo e retornar ao menu, digite P.\n")

                c = input("Digite o número para calcular: ")

                if flag == 0:    
                    cal = float(c)
                    flag = flag + 1
                else:
                    if c.upper() != "P":
                        cal = cal // float(c)
                    else:
                        print(cal)
                        break
