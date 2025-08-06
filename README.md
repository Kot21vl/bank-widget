# Bank Widget

## Описание
Проект виджета отображения банковских операций для клиента. Обрабатывает и маскирует данные о банковских картах и счетах.

## Установка
```bash
git clone https://github.com/Kot21vl/bank-widget
cd bank-wiget
poetry install

## Тестирование

Для запуска тестов используйте:
```bash
pytest --cov=src --cov-report=html

## Генераторы

В модуле `generators` реализованы функции:

- `filter_by_currency(transactions, currency)` — фильтрация по валюте.
- `transaction_descriptions(transactions)` — генерация описаний транзакций.
- `card_number_generator(start, end)` — генерация номеров карт.

### Пример использования:

```python
from src.generators import filter_by_currency, transaction_descriptions

usd_ops = filter_by_currency(transactions, "USD")
print(next(usd_ops))

for description in transaction_descriptions(transactions):
    print(description)
