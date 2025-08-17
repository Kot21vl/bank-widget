from typing import Any
from typing import Dict
from typing import List

from src.processing import filter_by_state
from src.processing import sort_by_date


# Тест для filter_by_state
def test_filter_by_state() -> None:
    data: List[Dict[str, Any]] = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    result = filter_by_state(data)
    assert result == [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]


# Тест для sort_by_date
def test_sort_by_date() -> None:
    data: List[Dict[str, Any]] = [
        {'id': 1, 'date': '2020-01-01T12:00:00'},
        {'id': 2, 'date': '2021-01-01T12:00:00'},
        {'id': 3, 'date': '2019-01-01T12:00:00'}
    ]
    result = sort_by_date(data)
    assert result == [
        {'id': 2, 'date': '2021-01-01T12:00:00'},
        {'id': 1, 'date': '2020-01-01T12:00:00'},
        {'id': 3, 'date': '2019-01-01T12:00:00'}
    ]
