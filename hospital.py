class queue():
    def __init__(self):
        self.put = []
    def add(self, x):
        self.put.append(x)
    def pop(self):
        if len(self.put) > 0:
            return self.put.pop(0)
    def isEmpty(self):
        if len(self.put) == 0:
            return True
        else:
            return False

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
            if critico.isEmpty == False:
                print(critico(0))
                critico.pop(0)
            elif grave.isEmpty == False:
                print(grave(0))
                grave.pop(0)
            elif leve.isEmpty == False:
                print(leve(0))
                leve.pop(0)
        case 3:
            print('\tEXCLUIR AGENDAMENTOS\n')
            x = input("Qual enfermidade deseja desmarcar? ")
            if x in critico:
                critico.pop(0)
            if x in grave:
                grave.pop(0)
            if x in leve:
                leve.pop(0)
        case 4:
            break
