from typing import Any
from typing import Dict
from typing import List


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по значению ключа "date".

    Аргументы:
        data: Список словарей, содержащих операции.
        descending: Флаг сортировки. Если True — сортировка по убыванию (сначала новые).

    Возвращает:
        Отсортированный список операций.
    """
    return sorted(
        data,
        key=lambda x: x.get("date") or "",
        reverse=descending
    )


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по полю 'state'.

    :param data: Список операций.
    :param state: Статус, по которому нужно отфильтровать (по умолчанию "EXECUTED").
    :return: Новый список, содержащий только операции с нужным статусом.
    """
    return [item for item in data if item.get("state") == state]
