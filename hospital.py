class queue():
    def __init__(self):
        self.put = []
    def add(self, x):
        self.put.append(x)
    def pop(self):
        if len(self.put) > 0:
            return self.put.pop(0)

while True:
    print("""
    >>>>>> HOSPITAL <<<<<<

    1 - Agendar Atendimento

    2 - Chamar Próximo Paciente

    3 - Excluir Agendamentos

    4 - Sair do Programa
        
    """)

    menu = int(input("Insira o numero equivalente ao item que deseja navegar: "))

    c = ['en1', 'en2', 'en3']
    g = ['en4', 'en5', 'en6']
    l = ['en7', 'en8', 'en9']
    
    critico = queue()
    grave = queue()
    leve = queue()

    match menu:
        case 1:
            print('\tAGENDAR ATENDIMENTO\n')
            nome = input('Insira aqui o nome do paciente: ')
            enfermidade = input('\nAgora insira a enfermidade do mesmo: ')
            if enfermidade in c:
                critico.add(enfermidade)
                print(critico.put)
            elif enfermidade in g:
                grave.add(enfermidade)
                print(grave.put)
            elif enfermidade in l:
                leve.add(enfermidade)
                print(leve.put)
        case 2:
            print('\tCHAMAR PROXIMO PACIENTE\n')
            
            
        case 3:
            print('\tEXCLUIR AGENDAMENTOS\n')
            
            
        case 4:
            break
