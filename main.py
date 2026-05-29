from gerenciador import GerenciadorDeReserva

hotel = GerenciadorDeReserva(nome="Hotel", cnpj="000.000.000/0001-00", endereco="Rua A, 123", telefone="1203-4556")
hotel.quartos("101", "Single", 200, "Disponível")
hotel.quartos("102", "Double", 350, "Disponível")
hotel.quartos("103", "Suite", 600, "Disponível")

while True:
    opcao = input("""
        1 - cadastrar
        2 - Verificar disponibilidade de quartos
        3 - Criar reserva
        4 - Modificar reserva
        5 - Cancelar Reserva
        6 - Reservas
        7 - Clientes
        8 - Quartos
        0 - Sair
        Escolha uma opção: """)

    match opcao:
        case "1":
            hotel.cadastro_clientes()
        case "2":
            hotel.verificar_disponibilidade_quartos()
        case "3":
            hotel.criar_reservas()
        case "4":
            hotel.modificar_reservas()
        case "5":
            hotel.cancelar_reservas()
        case "6":
            hotel.get_reserva()
        case "7":
            hotel.get_clientes()
        case "8":
            hotel.get_quartos()
        case "0":
            print("Saindo do sistema!")
            break
