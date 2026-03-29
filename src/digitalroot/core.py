from typing import Union, List, Tuple


def digital_root(n: Union[int, str]) -> int:
    """
    Вычисляет цифровой корень числа.
    
    Args:
        n: число (int) или строка с числом
        
    Returns:
        цифровой корень (число от 0 до 9)
        
    Raises:
        ValueError: если входное значение не является числом
        
    Example:
        >>> digital_root(123)
        6
    """
    if isinstance(n, int):
        if n < 0:
            n = abs(n)
        s = str(n)
    elif isinstance(n, str):
        s = n.lstrip('-')
        if not s.isdigit():
            raise ValueError(f"'{n}' is not a valid number")
    else:
        raise ValueError(f"Expected int or str, got {type(n).__name__}")
    
    if not s:
        return 0
    
    total = sum(int(digit) for digit in s)
    
    if total < 10:
        return total
    
    return digital_root(total)


def digital_root_with_steps(n: Union[int, str]) -> Tuple[int, List[int]]:
    """
    Вычисляет цифровой корень и возвращает все промежуточные суммы.
    
    Args:
        n: число или строка с числом
        
    Returns:
        кортеж (цифровой_корень, [список_промежуточных_сумм])
        
    Example:
        >>> digital_root_with_steps(987)
        (6, [24, 6])
    """
    if isinstance(n, int):
        if n < 0:
            n = abs(n)
        s = str(n)
    elif isinstance(n, str):
        s = n.lstrip('-')
        if not s.isdigit():
            raise ValueError(f"'{n}' is not a valid number")
    else:
        raise ValueError(f"Expected int or str, got {type(n).__name__}")
    
    if not s:
        return 0, []
    
    total = sum(int(digit) for digit in s)
    
    if total < 10:
        return total, [total]
    
    root, steps = digital_root_with_steps(total)
    return root, [total] + steps


def digital_root_fast(n: int) -> int:
    """
    Быстрое вычисление цифрового корня по математической формуле O(1).
    
    Формула: dr(n) = 1 + (|n| - 1) % 9, при n ≠ 0
             dr(0) = 0
    
    Args:
        n: целое число
        
    Returns:
        цифровой корень
        
    Example:
        >>> digital_root_fast(123)
        6
    """
    if n == 0:
        return 0
    if n < 0:
        n = abs(n)
    return 1 + (n - 1) % 9


def digital_root_batch(numbers: List[Union[int, str]]) -> List[int]:
    """
    Вычисляет цифровые корни для списка чисел.
    
    Args:
        numbers: список чисел или строк
        
    Returns:
        список цифровых корней
        
    Example:
        >>> digital_root_batch([123, 987, 0])
        [6, 6, 0]
    """
    return [digital_root(num) for num in numbers]


def is_digital_root_valid(n: int, expected_root: int) -> bool:
    """
    Проверяет, является ли expected_root цифровым корнем числа n.
    
    Args:
        n: исходное число
        expected_root: предполагаемый цифровой корень
        
    Returns:
        True если expected_root является цифровым корнем n
    """
    return digital_root(n) == expected_root