# atividade12.py

P1 = float(input("Insira o valor da primeira avaliação: "))
P2 = float(input("Insira o valor da segunda avaliação: "))

media = (P1 + (P2 * 2)) // 3

if media >= 70:
    print(f"Parabéns, você passou! Sua média é: {media}")
else:
    print(f"Que pena, você não passou! Sua média é: {media}")