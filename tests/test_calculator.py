from calculator.calculator import calculate
import pytest


def test_add():
    assert calculate(2, "+", 3) == 5


def test_subtract():
    assert calculate(5, "-", 2) == 3


def test_multiply():
    assert calculate(4, "*", 3) == 12


def test_divide():
    assert calculate(10, "/", 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(5, "/", 0)


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(5, "%", 2)
