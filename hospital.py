while True:
    print("""
    >>>>>> HOSPITAL <<<<<<

    1 - Agendar Atendimento

    2 - Chamar Próximo Paciente

    3 - Excluir Agendamentos

    4 - Sair do Programa
        
    """)

    menu = input(int("Insira o numero equivalente ao item que deseja navegar: "))

    

    match menu:
        case 1:
            print('\tAGENDAR ATENDIMENTO\n')
            nome = input('Insira aqui o nome do paciente: ')
            enfermidade = input('\nAgora insira a enfermidade do mesmo: ')
            break
        case 2:
            print('\tCHAMAR PROXIMO PACIENTE\n')
            
            break
        case 3:
            print('\tEXCLUIR AGENDAMENTOS\n')
            
            break
        case 4:
            break
