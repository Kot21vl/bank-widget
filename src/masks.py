def get_mask_card_number(card_number: int | str) -> str:
    """
    Маскирует номер банковской карты по шаблону: XXXX XX** **** XXXX

    :param card_number: номер карты (целое число из 16 цифр)
    :return: маскированный номер карты
    """
    number_str = str(card_number).rjust(16, "0")
    return f"{number_str[:4]} {number_str[4:6]}** **** {number_str[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """
    Маскирует номер банковского счёта по шаблону: **XXXX

    :param account_number: номер счёта (целое число)
    :return: маскированный номер счёта
    """
    number_str = str(account_number)
    return f"**{number_str[-4:]}"
