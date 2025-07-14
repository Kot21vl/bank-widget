def get_date(iso_date_str: str) -> str:
    """
    Принимает дату в ISO-формате (пример: '2024-03-11Т02:26:18.671407')
    и возвращает строку в формате 'ДД.ММ.ГГГГ' (пример: '11.03.2024').

    :param iso_date_str:
    :return:
    """
    date_part = iso_date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
