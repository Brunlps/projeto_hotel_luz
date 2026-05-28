class Cliente:

    def __init__(self, id_cliente: int, nome: str, telefone: str, email: str):
        self.id_cliente: int = id_cliente
        self.nome: str = nome
        self.telefone: str = telefone
        self.email: str = email

    def __str__(self):
        return f"[ID: {self.id_cliente}] {self.nome} | {self.telefone} | {self.email}"



class Quarto: 

    def __init__(self, numero_quarto: str, tipo_quarto: str, preco_diaria: float, status: str):
        self.numero_quarto: str = numero_quarto
        self.tipo_quarto: str = tipo_quarto
        self.preco_diaria: float = preco_diaria
        self.status: str = status

    def __str__(self):
        return f"Quarto: {self.numero_quarto}: {self.tipo_quarto} | {self.preco_diaria} | {self.status}"


class Reserva:
    def __init__(self, dono_reserva: Cliente, quarto_resevado: Quarto, data_check_in: str, data_check_out: str, status_reserva: str):
        self.dono_reserva: Cliente = dono_reserva
        self.quarto_resevado: Quarto = quarto_resevado
        self.data_check_in: str = data_check_in
        self.data_check_out: str = data_check_out
        self.status_reserva: str = status_reserva

    def __str__(self):
        return f"Cliente: {self.dono_reserva} | {self.quarto_resevado} | {self.data_check_in} | {self.data_check_out} | {self.status_reserva}"


class GerenciadorDeReserva(Cliente, Quarto, Reserva):

    def __init__(self, nome: str, cnpj: str, endereco: str, telefone: str):
        self.nome: str = nome
        self.cnpj: str = cnpj
        self.endereco: str = endereco
        self.telefone: str = telefone
        self.id_atual: int = 1
        self.lista_clientes: list[Cliente] = []
        self.lista_quartos: list[Quarto] = []
        self.historico_reservas: list[Reserva] = []

    def quartos(self, numero_quarto: str, tipo_quarto: str, preco_diaria: float, status: str) -> None:
        novo_quarto = Quarto(numero_quarto, tipo_quarto, preco_diaria, status="Disponível")

        self.lista_quartos.append(novo_quarto)

    def cadastro_clientes(self) -> Cliente:

        print("-=-=-=-=-=-=-=Clientes=-=-==-=-=-=-=-")
        self.nome = input("Nome: ")
        self.email = input("E-mail: ")
        self.telefone = input("Telefone: ")

        novo_cliente = Cliente(id_cliente= self.id_atual, 
                               nome= self.nome, 
                               telefone= self.telefone, 
                               email=self.email)

        self.lista_clientes.append(novo_cliente)

        self.id_atual += 1

        return novo_cliente

    def verificar_disponibilidade_quartos(self) -> None:

        for quartos in self.lista_quartos:
            if quartos.status == "Disponível":
                print(f"Quartos disponíveis: {quartos}")

    def criar_reservas(self) -> None:

        # Buscando clientes
        id_buscador = int(input("ID do cliente: "))

        cliente_encotrado = None

        for cliente in self.lista_clientes:
            if cliente.id_cliente == id_buscador:
                cliente_encotrado = cliente

        if cliente_encotrado is None:
            print("Cliente não encontrado.")
            return
        
        # Buscando quartos
        numero_buscador = input("Número do quarto: ")

        quarto_encotrado = None

        for quarto in self.lista_quartos:
            if quarto.numero_quarto == numero_buscador:
                if quarto.status == "Disponível":
                    quarto_encotrado = quarto

        if quarto_encotrado is None:
            print("Quarto não encontrado.")
            return
        
        # Add datas
        data_check_in = input("Data de check-in (dd/mm/aaaa): ")
        data_check_out = input("Data de check-out (dd/mm/aaaa): ")

        # Criando Reserva
        nova_reserva = Reserva(
            dono_reseva=cliente_encotrado,
            quarto_resevado=quarto_encotrado,
            data_check_in=data_check_in,
            data_check_out=data_check_out,
            status_reserva="Ativa")
        
        self.historico_reservas.append(nova_reserva)

        quarto_encotrado.status = "Ocupado"

        print("Reserva criada com sucesso!")

    def modificar_reservas(self) -> None:

        id_buscador = int(input("ID do cliente: "))

        reserva_encotrado = None

        for reserva in self.historico_reservas:

            if reserva.dono_reserva.id_cliente == id_buscador:
                reserva_encotrado = reserva

        if reserva_encotrado is None:
            print("Reserva não encontrado.")
            return

        print(f"Reserva atual: {reserva_encotrado}")

        # Add datas
        nova_data_check_in = input("Nova Data de check-in (dd/mm/aaaa): ")
        nova_data_check_out = input("Nova Data de check-out (dd/mm/aaaa): ")

        reserva_encotrado.data_check_in = nova_data_check_in
        reserva_encotrado.data_check_out = nova_data_check_out

        print("Reserva modificada com sucesso!")

    def cancelar_reservas(self) -> None:
        id_buscador = int(input("ID do cliente: "))

        reserva_encotrado = None

        for reserva in self.historico_reservas:
            if reserva.dono_reserva.id_cliente == id_buscador:
                reserva_encotrado = reserva

        if reserva_encotrado is None:
            print("Reserva não encontrado.")
            return

        reserva_encotrado.status_reserva = "Cancelada"
        reserva_encotrado.quarto_resevado.status = "Disponível"

        print("Reserva cancelada com sucesso!")


    def get_reserva(self) -> None:

        for reserva in self.historico_reservas:
            # i += 1
            print(f"""
                  =-=-=-=-=Reservas-=-=-=-=
                  {reserva}""")

        return

    def get_clientes(self) -> None:

        for cliente in self.lista_clientes:
            print(cliente)
        return

    def get_quartos(self) -> None:

        for quarto in self.lista_quartos:
            print(quarto)
        return




# print(client = Reserva.cadastro_clientes)

# Hotel e quartos
hotel = GerenciadorDeReserva(nome="Hotel", cnpj="000.000.000/0001-00", endereco="Rua A, 123", telefone="1203-4556")
hotel.quartos("101", "Single", 200, "Disponível")
hotel.quartos("102", "Double", 350, "Disponível")
hotel.quartos("103", "Suite", 600, "Disponível")


while True:

    opcao = input("""
        1 - cadastrar
        2 - Verificar disponibilidade de quartos
        3 - Criar reserva
        4 - Modificar reservar
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