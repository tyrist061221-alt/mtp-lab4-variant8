"""Лабораторная работа №4: демонстрация всех заданий варианта 8.

Запуск: python main.py
"""

from tasks.povysh_1_compose import compose
from tasks.povysh_8_csv import process_csv
from tasks.sredn_10_multi_map import apply_functions
from tasks.sredn_4_factorial import factorial
from tasks.sredn_8_timer import measure_time


def demo_timer() -> None:
    print("=" * 60)
    print("Средн.1 — задание 8: декоратор замера времени")
    print("=" * 60)

    @measure_time
    def slow_sum(count):
        total = 0
        for number in range(1, count + 1):
            total += number
        return total

    print("Результат slow_sum(1000000):", slow_sum(1_000_000))
    print(f"Время выполнения: {slow_sum.last_duration:.6f} сек.")
    print()


def demo_multi_map() -> None:
    print("=" * 60)
    print("Средн.2 — задание 10: несколько функций к списку через map")
    print("=" * 60)
    numbers = [1, 2, 3, 4, 5]
    functions = [lambda x: x ** 2, lambda x: x + 1]
    print("Исходный список:", numbers)
    print("Квадраты и +1:", apply_functions(numbers, functions))
    print()


def demo_factorial() -> None:
    print("=" * 60)
    print("Средн.3 — задание 4: факториал через reduce")
    print("=" * 60)
    for n in [0, 1, 5, 10]:
        print(f"{n}! = {factorial(n)}")
    print()


def demo_csv() -> None:
    print("=" * 60)
    print("Повыш.1 — задание 8: фильтрация и преобразование CSV")
    print("=" * 60)
    import os

    base = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base, "data", "students.csv")
    destination = os.path.join(base, "data", "students_passed.csv")
    written = process_csv(source, destination, min_score=60)
    print(f"Прошли фильтр (балл >= 60): {written} записей")
    print("Результат:", destination)
    print()


def demo_compose() -> None:
    print("=" * 60)
    print("Повыш.2 — задание 1: композиция функций (compose)")
    print("=" * 60)
    combined = compose(lambda x: x * 2, lambda x: x + 3)
    print("compose(double, add_three)(4) =", combined(4))
    pipeline = compose(str.strip, str.lower)
    print("Обработка строки:", pipeline("  ПРИВЕТ  "))
    print()


if __name__ == "__main__":
    demo_timer()
    demo_multi_map()
    demo_factorial()
    demo_csv()
    demo_compose()
    print("Все задания варианта 8 выполнены.")
