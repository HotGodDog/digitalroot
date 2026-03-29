import pytest
from digitalroot.core import digital_root


def test_single_digit():
    """Однозначные числа возвращают себя же"""
    for i in range(10):
        assert digital_root(i) == i


def test_two_digits():
    """Двузначные числа"""
    assert digital_root(10) == 1
    assert digital_root(11) == 2
    assert digital_root(99) == 9


def test_three_digits():
    """Трехзначные числа"""
    assert digital_root(123) == 6
    assert digital_root(987) == 6
    assert digital_root(999) == 9


def test_large_number():
    """Большие числа"""
    assert digital_root(123456789) == 9


def test_zero():
    """Ноль"""
    assert digital_root(0) == 0


def test_negative():
    """Отрицательные числа"""
    assert digital_root(-123) == 6
    assert digital_root(-999) == 9


def test_string_input():
    """Ввод строкой"""
    assert digital_root("123") == 6
    assert digital_root("987") == 6
    assert digital_root("0") == 0
    assert digital_root("-123") == 6


def test_invalid_string():
    """Некорректная строка"""
    with pytest.raises(ValueError):
        digital_root("abc")
    
    with pytest.raises(ValueError):
        digital_root("12a3")


def test_invalid_type():
    """Некорректный тип"""
    with pytest.raises(ValueError):
        digital_root(3.14)
    
    with pytest.raises(ValueError):
        digital_root(None)