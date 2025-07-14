from src.masks import get_mask_card_number, get_mask_account


def get_date(iso_date_str: str) -> str:
    """
    Принимает дату в ISO-формате (пример: '2024-03-11Т02:26:18.671407')
    и возвращает строку в формате 'ДД.ММ.ГГГГ' (пример: '11.03.2024').

    :param iso_date_str: строка в ISO-формате
    :return: строка в формате ДД.ММ.ГГГГ
    """
    date_part = iso_date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


def mask_account_card(info: str) -> str:
    """
     Принимает строку с типом и номером карты или счета и возвращает строку
    с замаскированным номером.

    :param info: строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"
    :return: строка с замаскированным номером
    """
    parts = info.rsplit(" ", maxsplit=1)
    if len(parts) != 2:
        return info

    card_type, number = parts

    if card_type.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"
