# tests/test_decorators.py
from pathlib import Path  # Добавим импорт

import pytest

from src.decorators import log


def test_log_to_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    res = add(2, 3)
    assert res == 5

    # capsys captures stdout/stderr; logging.StreamHandler пишет в stderr
    captured = capsys.readouterr()
    assert "Called add" in captured.err
    assert "returned" in captured.err


def test_log_to_console_exception(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def fail() -> None:
        raise ValueError("oops")

    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()
    # должно быть сообщение об исключении
    assert "Exception in fail" in captured.err or "Traceback" in captured.err


def test_log_to_file_success(tmp_path: Path) -> None:
    logfile = tmp_path / "mylog.log"

    @log(filename=str(logfile))
    def greet(name: str) -> str:
        return f"Hello, {name}"

    res = greet("Alex")
    assert res == "Hello, Alex"

    content = logfile.read_text(encoding="utf-8")
    assert "Called greet" in content
    assert "returned" in content


def test_log_to_file_exception(tmp_path: Path) -> None:
    logfile = tmp_path / "errlog.log"

    @log(filename=str(logfile))
    def boom() -> None:
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        boom()

    content = logfile.read_text(encoding="utf-8")
    assert "Exception in boom" in content or "Traceback" in content


def test_decorator_without_parentheses_works(
    capsys: pytest.CaptureFixture[str],
) -> None:
    # использование @log без скобок
    @log
    def mul(a: int, b: int) -> int:
        return a * b

    assert mul(3, 4) == 12
    captured = capsys.readouterr()
    assert "Called mul" in captured.err
