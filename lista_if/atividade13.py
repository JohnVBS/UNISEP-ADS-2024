n1 = float(input("Insira a nota do trabalho de laboratório: "))
n2 = float(input("Agora, a nota da avaliação semestral: "))
n3 = float(input("Por fim, a nota do exame final: "))

if (n1 >=0 and n1 <=10) and (n2 >=0 and n2 <=10) and (n3 >=0 and n3 <=10):
    peso1 = n1 * 2
    peso2 = n2 * 3
    peso3 = n3 * 5
    peso = peso1 + peso2 + peso3
    nota = peso // 10
    if nota >=0 and nota <=2.9:
        print("O aluno está reprovado!")
    elif nota >=3.0 and nota <=4.9:
        print("O aluno está de recuperação")
    else:
        print("O aluno foi aprovado!")
else:
    print("Um ou mais notas estão inválidas")
    