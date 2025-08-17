from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.processing import filter_by_state
from src.processing import sort_by_date

if __name__ == "__main__":
    # Пример номера карты и счёта
    card_number = 1234567812345678
    account_number = 40817810099910004312

    # Печатаем маскированные значения
    print("Маскированный номер карты:", get_mask_card_number(card_number))
    print("Маскированный номер счёта:", get_mask_account(account_number))

    print()  # пустая строка для отделения блоков вывода

    # Пример данных операций
    data = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2020-01-01T12:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2021-01-01T12:00:00'}
    ]

    # Фильтрация и сортировка операций
    filtered = filter_by_state(data)
    sorted_data = sort_by_date(data)

    print("Отфильтрованные операции (только EXECUTED):", filtered)
    print("Отсортированные операции по дате (по убыванию):", sorted_data)
