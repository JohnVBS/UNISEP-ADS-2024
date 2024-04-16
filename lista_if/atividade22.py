# atividade22.py

pro = float(input("Primeiro, insira o valor do produto: "))
est = int(input('''
Agora, o Estado que esse produto será destinado:
[ 1 ]  MG
[ 2 ]  SP
[ 3 ]  RJ
[ 4 ]  MS
'''))

if est >=1 and est <=4:
    match est:
        case 1:
            print("\nVocê escolheu MG")
            mg = (pro * 7) / 100
            final = pro + mg
            print(f"O valor total será {final}")
        case 2:
            print("\nVocê escolheu SP")
            sp = (pro * 12) / 100
            final = pro + sp
            print(f"O valor total será {final}")
        case 3:
            print("\nVocê escolheu RJ")
            rj = (pro * 15) / 100
            final = pro + rj
            print(f"O valor total será {final}")
        case 4:
            print("\nVocê escolheu MS")
            ms = (pro * 8) / 100
            final = pro + ms
            print(f"O valor total será {final}")
else:
    print("Número inválido")