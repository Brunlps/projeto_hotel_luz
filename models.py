class Cliente:
    def __init__(self, id_cliente: int, nome: str, telefone: str, email: str):
        self.id_cliente: int = id_cliente
        self.nome: str = nome
        self.telefone: str = telefone
        self.email: str = email

    def __str__(self) -> str:
        return f"[ID: {self.id_cliente}] {self.nome} | {self.telefone} | {self.email}"


class Quarto:
    def __init__(self, numero_quarto: str, tipo_quarto: str, preco_diaria: float, status: str):
        self.numero_quarto: str = numero_quarto
        self.tipo_quarto: str = tipo_quarto
        self.preco_diaria: float = preco_diaria
        self.status: str = status

    def __str__(self) -> str:
        return f"Quarto {self.numero_quarto}: {self.tipo_quarto} | R${self.preco_diaria} | {self.status}"


class Reserva:
    def __init__(self, id_reserva: int, dono_reserva: Cliente, quarto_reservado: Quarto, data_check_in: str, data_check_out: str, status_reserva: str):
        self.id_reserva: int = id_reserva
        self.dono_reserva: Cliente = dono_reserva
        self.quarto_reservado: Quarto = quarto_reservado
        self.data_check_in: str = data_check_in
        self.data_check_out: str = data_check_out
        self.status_reserva: str = status_reserva

    def __str__(self) -> str:
        return f"[Reserva ID: {self.id_reserva}] Cliente: {self.dono_reserva} | {self.quarto_reservado} | {self.data_check_in} | {self.data_check_out} | {self.status_reserva}"
