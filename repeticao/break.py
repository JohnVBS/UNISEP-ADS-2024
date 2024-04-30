# break.py

for n in range(500):
    print(f"N: {n}")
    if n == 50:
        break
        # O break quebra o laço e bota um fim em tudo!

for n in range(10):
    if n % 3 == 0:
        continue
        # O continue pula a rodada no loop e vai para a próxima!
    print(f"N: {n}")

while True:
    opcao = input("Digite X para sair: ")
    print(opcao)
    if opcao.upper() == "X":
        break
