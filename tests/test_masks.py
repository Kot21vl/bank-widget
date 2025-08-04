# test_masks.py
import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_test_data():
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ]

def test_get_mask_card_number(card_test_data):
    for card_number, expected in card_test_data:
        assert get_mask_card_number(card_number) == expected

@pytest.fixture
def account_test_data():
    return [
        ("12345678901234567890", "**7890"),
        ("00000000000000001234", "**1234"),
    ]

def test_get_mask_account(account_test_data):
    for account_number, expected in account_test_data:
        assert get_mask_account(account_number) == expected
