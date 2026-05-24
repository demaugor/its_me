import math
from typing import Union


def range_gcd_pseudo(l: int, r: int) -> int:
    """Вычисляет наибольший общий делитель для последовательности целых чисел.

    Математический факт: НОД любых двух последовательных целых чисел равен 1.
    Следовательно, для любого диапазона длиной > 1 (хотя бы два различных числа)
    НОД всей последовательности также будет равен 1.

    Исключения:
    - Если l == r (диапазон из одного числа) → НОД = |l|
    - Если диапазон содержит только нули (0,0) → НОД = 0
    - Если в диапазоне есть ноль И другие числа → НОД = 1 (так как gcd(0, x) = |x|, а |x| и следующее число дадут 1)

    :param l: левая граница диапазона (включительно)
    :param r: правая граница диапазона (включительно)
    :return: НОД всех чисел в диапазоне

    :perf: O(1) по времени и памяти
    """
    assert r >= l, f"Левая граница ({l}) должна быть ≤ правой ({r})"
    
    # Диапазон из одного числа
    if l == r:
        return abs(l)
    
    # Диапазон из двух и более чисел → НОД = 1
    # Это работает даже для случаев с нулём, например [0, 1] → gcd(0,1) = 1
    return 1


def range_gcd_actual(l: int, r: int) -> int:
    """Нативное решение через math.gcd для всех чисел диапазона.
    
    Сложность: O(n * log M), где n = r-l+1, M = максимальное число в диапазоне.
    Используется только для верификации псевдо-решения.
    """
    if l == r:
        return abs(l)
    
    result = 0
    for num in range(l, r + 1):
        result = math.gcd(result, num)
    return abs(result)


# Более эффективная версия actual (с частичным вычислением)
def range_gcd_actual_fast(l: int, r: int) -> int:
    """Оптимизированная версия: останавливаемся, как только НОД стал равен 1."""
    if l == r:
        return abs(l)
    
    result = 0
    for num in range(l, r + 1):
        result = math.gcd(result, num)
        if result == 1:  # Ранний выход: дальше хуже не будет
            return 1
    return abs(result)


if __name__ == "__main__":
    test_cases = [
        # (l, r, expected)
        (1, 10, 1),           # последовательные числа
        (5, 5, 5),            # одно число
        (-10, -5, 1),         # отрицательные последовательные
        (-10, -10, 10),       # одно отрицательное число
        (0, 0, 0),            # только ноль
        (0, 10, 1),           # ноль и последовательные числа
        (-10, 0, 1),          # отрицательные последовательные включая ноль
        (100, 101, 1),        # любые два последовательных числа
        (-3, -2, 1),          # отрицательные последовательные
        (2, 3, 1),            # простые последовательные
        (1000000, 1000001, 1),# большие последовательные числа
    ]
    
    for l, r, expected in test_cases:
        # Проверяем псевдо-решение
        pseudo_result = range_gcd_pseudo(l, r)
        assert pseudo_result == expected, \
            f"range_gcd_pseudo({l}, {r}) = {pseudo_result} (expected: {expected})"
        
        # Проверяем, что псевдо-решение совпадает с реальным вычислением
        actual_result = range_gcd_actual_fast(l, r)
        assert pseudo_result == actual_result, \
            f"❌ РАСХОЖДЕНИЕ: pseudo={pseudo_result}, actual={actual_result} for ({l}, {r})"
        
        print(f" GCD({l}, {r}) = {pseudo_result}")
    
    print("\n Все тесты пройдены!")
    
    # Демонстрация производительности
    import timeit
    
    print("\n Сравнение производительности (диапазон 1..10000):")
    
    time_pseudo = timeit.timeit(
        "range_gcd_pseudo(1, 10000)",
        globals=globals(),
        number=100000
    )
    print(f"  Псевдо-решение O(1):      {time_pseudo:.5f} сек (100k вызовов)")
    
    time_actual_fast = timeit.timeit(
        "range_gcd_actual_fast(1, 10000)",
        globals=globals(),
        number=100
    )
    print(f"  Реальное решение с ранним выходом: {time_actual_fast:.5f} сек (100 вызовов)")