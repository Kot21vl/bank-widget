from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по значению ключа 'state'.

    :param data: Список операций (словарей).
    :param state: Значение фильтра по ключу 'state'. По умолчанию 'EXECUTED'.
    :return: Отфильтрованный список операций.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param data: Список операций (словарей).
    :param descending: Порядок сортировки: убывание (по умолчанию) или возрастанию.
    :return: Отсортированный список операций.
    """
    return sorted(data, key=lambda x: x.get("date"), reverse=descending)