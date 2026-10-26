"""Задание 8 (средней сложности): декоратор замера времени работы функции.

Реализован декоратор measure_time на time.perf_counter().
Декоратор возвращает исходный результат функции и сохраняет
длительность последнего вызова в атрибуте last_duration.
Декоратор корректно измеряет время даже при исключении (try/finally)
и сохраняет метаданные функции благодаря functools.wraps.
"""

import functools
import time


def measure_time(func):
    """Декоратор: замеряет время выполнения функции."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_duration = time.perf_counter() - start

    wrapper.last_duration = None
    return wrapper


if __name__ == "__main__":
    @measure_time
    def slow_sum(count):
        """Суммирует числа от 1 до count (имитация нагрузки)."""
        total = 0
        for number in range(1, count + 1):
            total += number
        return total

    result = slow_sum(1_000_000)
    print("Результат slow_sum:", result)
    print(f"Время выполнения: {slow_sum.last_duration:.6f} сек.")

    @measure_time
    def failing():
        raise ValueError("Ошибка внутри функции")

    try:
        failing()
    except ValueError:
        print("Исключение проброшено наружу, время всё равно измерено:",
              f"{failing.last_duration:.6f} сек.")
