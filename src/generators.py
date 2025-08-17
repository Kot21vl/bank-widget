from typing import Dict
from typing import Iterator
from typing import List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield (
            f"{formatted_number[:4]} "
            f"{formatted_number[4:8]} "
            f"{formatted_number[8:12]} "
            f"{formatted_number[12:]}"
        )
