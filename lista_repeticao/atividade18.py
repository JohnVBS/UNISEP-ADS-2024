#atividade18.py

lista = []

while True:
    qua = int(input("Insira a quantidade de elementos que a lista deve ter: "))

    for n in range(qua):
        num = float(input("Insira um número ou digite 'X' para sair: "))
        lista.append(num)

    lista.sort()

    print(lista(qua))
