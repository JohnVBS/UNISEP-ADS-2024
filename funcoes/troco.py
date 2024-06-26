#funcoes/troco.py

def ler():
    valor = float(input("Digite o valor: "))
    return valor


def qtd_notas(valor, nota):
    if valor >= nota:
        qtd = valor // nota
        valor = valor - (qtd * nota)
        print(f"{qtd} nota(s) de R$ {nota:.2f}")
    return valor


notas = (200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01)

valor = ler()
for nota in notas:
    valor = qtd_notas(valor, nota)
print("Obrigado e volte sempre")
