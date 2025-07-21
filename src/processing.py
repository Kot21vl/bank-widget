from typing import List, Dict, Any

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

