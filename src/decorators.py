# src/decorators.py
import logging
from functools import wraps
from typing import Callable
from typing import Optional
from typing import ParamSpec
from typing import TypeVar
from typing import overload

P = ParamSpec("P")
R = TypeVar("R")


def _decorate(func: Callable[P, R], filename: Optional[str]) -> Callable[P, R]:
    """
    Внутренняя функция-декоратор: создаёт логгер, оборачивает функцию.
    Handler добавляется на каждый вызов и удаляется по завершении вызова,
    чтобы не было дублирования сообщений при повторных вызовах.
    """
    logger_name = f"{func.__module__}.{func.__name__}.{id(func)}"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    # не будем использовать propagate, чтобы не дублировать вывод в root-логгер
    logger.propagate = False

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        # создаём handler при каждом вызове — чтобы можно было логировать в разные файлы
        handler: logging.Handler
        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()  # по умолчанию в stderr

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        try:
            logger.info("Called %s with args=%s kwargs=%s", func.__name__, args, kwargs)
            result = func(*args, **kwargs)
            logger.info("%s returned %r", func.__name__, result)
            return result
        except Exception as exc:  # log exception and reraise
            # logger.exception добавляет stack trace
            logger.exception(
                "Exception in %s: %s; args=%s kwargs=%s", func.__name__, type(exc).__name__, args, kwargs
            )
            raise
        finally:
            # убрать handler и закрыть ресурс
            logger.removeHandler(handler)
            handler.close()

    return wrapper


# поддерживаем вызов как @log и как @log(filename="file.log")
@overload
def log(func: Callable[P, R]) -> Callable[P, R]:  # type: ignore[misc]
    ...


@overload
def log(*, filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    ...


def log(
    func: Optional[Callable[P, R]] = None,
    *,
    filename: Optional[str] = None
) -> Callable[[Callable[P, R]], Callable[P, R]] | Callable[P, R]:
    """
    Декоратор для логирования вызовов функций.

    Можно использовать так:
    @log
    def f(...): ...

    или с параметром:
    @log(filename="my.log")
    def f(...): ...

    Лог содержит: время, уровень, имя функции, аргументы, результат или сообщение об ошибке.
    Если filename задан — логи пишутся в файл, иначе — в консоль (stderr).
    """
    if func is None:
        return lambda f: _decorate(f, filename)
    return _decorate(func, filename)
