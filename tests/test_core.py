import pytest
from digitalroot.core import (
    digital_root,
    digital_root_with_steps,
    digital_root_fast,
    digital_root_batch,
    is_digital_root_valid,
)


# ============= Тесты для digital_root =============

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


# ============= Тесты для digital_root_with_steps =============

def test_with_steps_single_digit():
    """Однозначное число"""
    root, steps = digital_root_with_steps(5)
    assert root == 5
    assert steps == [5]


def test_with_steps_two_digits():
    """Двузначное число"""
    root, steps = digital_root_with_steps(99)
    assert root == 9
    assert steps == [18, 9]


def test_with_steps_three_digits():
    """Трехзначное число"""
    root, steps = digital_root_with_steps(987)
    assert root == 6
    assert steps == [24, 6]


def test_with_steps_negative():
    """Отрицательное число"""
    root, steps = digital_root_with_steps(-123)
    assert root == 6
    assert steps == [6]


# ============= Тесты для digital_root_fast =============

def test_fast_vs_regular():
    """Сравнение быстрой и обычной версии"""
    for n in range(1, 1000):
        assert digital_root_fast(n) == digital_root(n)


def test_fast_zero():
    """Ноль"""
    assert digital_root_fast(0) == 0


def test_fast_negative():
    """Отрицательные числа"""
    assert digital_root_fast(-123) == digital_root_fast(123)


# ============= Тесты для digital_root_batch =============

def test_batch():
    """Пакетная обработка"""
    result = digital_root_batch([123, 987, 999, 0])
    assert result == [6, 6, 9, 0]


def test_batch_with_strings():
    """Пакетная обработка со строками"""
    result = digital_root_batch(["123", "987", "999", "0"])
    assert result == [6, 6, 9, 0]


def test_batch_empty():
    """Пустой список"""
    result = digital_root_batch([])
    assert result == []


# ============= Тесты для is_digital_root_valid =============

def test_valid():
    """Корректные пары"""
    assert is_digital_root_valid(123, 6) is True
    assert is_digital_root_valid(987, 6) is True
    assert is_digital_root_valid(999, 9) is True


def test_invalid():
    """Некорректные пары"""
    assert is_digital_root_valid(123, 5) is False
    assert is_digital_root_valid(987, 9) is False