"""Задание 4 (средней сложности): факториал через reduce.

Факториал вычисляется свёрткой functools.reduce по произведению
всех целых чисел от 1 до n. Начальное значение 1 обеспечивает
корректность 0! = 1. Отрицательные и нецелые аргументы
отклоняются с понятными исключениями.
"""

import operator
from functools import reduce


def factorial(n: int) -> int:
    """Возвращает n! через reduce(operator.mul, ...).

    0! = 1. Отрицательные и нецелые значения запрещены.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Факториал определён только для целых чисел")
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    return reduce(operator.mul, range(1, n + 1), 1)


if __name__ == "__main__":
    for n in [0, 1, 5, 10]:
        print(f"{n}! = {factorial(n)}")
    try:
        factorial(-3)
    except ValueError as error:
        print("Ошибка:", error)
    try:
        factorial(2.5)
    except TypeError as error:
        print("Ошибка:", error)
