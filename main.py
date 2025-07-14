from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    # Пример номера карты и счёта
    card_number = 1234567812345678
    account_number = 40817810099910004312

    # Печатаем маскированные значения
    print("Маскированный номер карты:", get_mask_card_number(card_number))
    print("Маскированный номер счёта:", get_mask_account(account_number))
