from src.widget import mask_account_card, get_date

## Тесты для mask_account_card
def test_mask_account_card_card():
    input_date = 'Visa Platinum 1245781456127458'
    expected = 'Visa Platinum 1245 78** **** 7458'
    assert mask_account_card(input_date) == expected


def test_mask_account_card_account():
    input_date = 'Счет 58518872554598981212'
    expected = 'Счет **1212'
    assert mask_account_card(input_date) == expected

# Тесты для get_date
def test_get_date():
    input_date = '2019-08-26T10:50:58.294041'
    expected = '26.08.2019'
    assert get_date(input_date) == expected
