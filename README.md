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

## Новый функционал

### Декоратор `log`
Добавлен модуль `decorators` с декоратором `log`, который позволяет логировать выполнение функций.

- **Поддержка логирования в консоль или в файл** — при передаче аргумента `filename` логи пишутся в файл, иначе выводятся в консоль.
- **Фиксируются**: имя функции, переданные аргументы, результат выполнения, а также ошибки (с типом и входными параметрами).
- **Пример использования**:
```python
from decorators import log

@log()
def add(a, b):
    return a + b

@log("log.txt")
def divide(a, b):
    return a / b
