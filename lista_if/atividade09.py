# atividade9.py

salario = float(input("Insira o valor do salário do trabalhador: "))
prestacao = float(input("Agora, o valor da prestação do empréstimo: "))
por = (salario*20)/100
if prestacao > por:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
