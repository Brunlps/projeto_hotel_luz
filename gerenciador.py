from models import Cliente, Quarto, Reserva


class GerenciadorDeReserva():
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

        cliente_encontrado = None

        for cliente in self.lista_clientes:
            if cliente.id_cliente == id_buscador:
                cliente_encontrado = cliente

        if cliente_encontrado is None:
            print("Cliente não encontrado.")
            return
        
        # Buscando quartos
        numero_buscador = input("Número do quarto: ")

        quarto_encontrado = None

        for quarto in self.lista_quartos:
            if quarto.numero_quarto == numero_buscador:
                if quarto.status == "Disponível":
                    quarto_encontrado = quarto

        if quarto_encontrado is None:
            print("Quarto não encontrado.")
            return
        
        # Add datas
        data_check_in = input("Data de check-in (dd/mm/aaaa): ")
        data_check_out = input("Data de check-out (dd/mm/aaaa): ")

        # Criando Reserva
        nova_reserva = Reserva(
            dono_reserva=cliente_encontrado,
            quarto_reservado=quarto_encontrado,
            data_check_in=data_check_in,
            data_check_out=data_check_out,
            status_reserva="Ativa")
        
        self.historico_reservas.append(nova_reserva)

        quarto_encontrado.status = "Ocupado"

        print("Reserva criada com sucesso!")

    def modificar_reservas(self) -> None:

        id_buscador = int(input("ID do cliente: "))

        reserva_encontrada = None

        for reserva in self.historico_reservas:

            if reserva.dono_reserva.id_cliente == id_buscador:
                reserva_encontrada = reserva

        if reserva_encontrada is None:
            print("Reserva não encontrado.")
            return

        print(f"Reserva atual: {reserva_encontrada}")

        # Add datas
        nova_data_check_in = input("Nova Data de check-in (dd/mm/aaaa): ")
        nova_data_check_out = input("Nova Data de check-out (dd/mm/aaaa): ")

        reserva_encontrada.data_check_in = nova_data_check_in
        reserva_encontrada.data_check_out = nova_data_check_out

        print("Reserva modificada com sucesso!")

    def cancelar_reservas(self) -> None:
        id_buscador = int(input("ID do cliente: "))

        reserva_encontrada = None

        for reserva in self.historico_reservas:
            if reserva.dono_reserva.id_cliente == id_buscador:
                reserva_encontrada = reserva

        if reserva_encontrada is None:
            print("Reserva não encontrado.")
            return

        reserva_encontrada.status_reserva = "Cancelada"
        reserva_encontrada.quarto_reservado.status = "Disponível"

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
