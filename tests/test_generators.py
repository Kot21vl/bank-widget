from typing import Dict
from typing import Iterator
from typing import List

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.fixture
def sample_transactions() -> List[Dict]:
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "USD Transaction",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "RUB Transaction",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Another USD Transaction",
        },
    ]


def test_filter_by_currency(sample_transactions: List[Dict]) -> None:
    usd_gen: Iterator[Dict] = filter_by_currency(sample_transactions, "USD")
    result = list(usd_gen)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_empty() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions: List[Dict]) -> None:
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "USD Transaction",
        "RUB Transaction",
        "Another USD Transaction",
    ]


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, end: int, expected: List[str]) -> None:
    result = list(card_number_generator(start, end))
    assert result == expected
