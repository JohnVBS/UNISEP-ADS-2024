# atividade16.py

bmn = float(input("Insira o valor da base menor do trapézio: "))
bm = float(input("Insira o valor da base maior do trapézio: "))
alt = float(input("Insira o valor da altura do trapézio: "))

if (bmn > 0) and (bm > 0) and (alt > 0):
    area= ((bm+bmn)*alt) // 2
    print(f"A área desse trapézio é: {area}")
else:
    print("Um ou mais números inválidos")
