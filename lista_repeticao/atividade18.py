#atividade18.py

limite = int(input("Digite até quantos: "))
maior = 0
qtd_maior = 0

for _ in range(limite):
    numero = int(input("Digite um numero: "))
    if numero > maior:
        maior = numero
        qtd_maior += 1

print(f"O maior foi {maior} e foi digitado {qtd_maior} vezes")
