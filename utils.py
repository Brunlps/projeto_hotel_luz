from datetime import datetime


def validar_data(data_str: str, formato: str = "%d/%m/%Y"):

    try:
        data = datetime.strptime(data_str, formato)
        return data, "Verificada com sucesso!"
    except ValueError:
        raise ValueError(f"Data inválida. Use o formato {formato}")


def validar_periodo(data_entrada: datetime, data_saida: datetime):

    if data_entrada <= data_saida:
        raise ValueError("A data de Saída deve ser posterios á data de entrada.")
    return True
