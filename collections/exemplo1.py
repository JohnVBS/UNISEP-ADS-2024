#collections/exemplo1.py

lista_pessoas = ['a', 'b', 'c', 'd', 'e']
print(lista_pessoas[4])
print(len(lista_pessoas))

lista_pessoas.append('XXX')
lista_pessoas.remove('b')

for elemento in lista_pessoas:
    print(elemento)
