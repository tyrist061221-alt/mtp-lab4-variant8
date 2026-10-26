"""Задание 10 (средней сложности): применить несколько функций к списку
через map.

Функция apply_functions принимает список значений и список функций
и возвращает результат применения каждой функции ко всем значениям:
для [1, 2, 3] и функций «квадрат», «+1» результат —
[[1, 4, 9], [2, 3, 4]]. Каждая функция применяется через map.
"""


def apply_functions(values, functions):
    """Применяет каждую функцию из functions ко всем values.

    Возвращает список результатов: по одному списку на функцию.
    """
    return [list(map(function, values)) for function in functions]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    functions = [
        lambda x: x ** 2,          # квадрат числа
        lambda x: x + 1,           # увеличить на один
        lambda x: -x,              # смена знака
    ]

    print("Исходный список:", numbers)
    for function, results in zip(functions, apply_functions(numbers, functions)):
        print(f"{function.__name__ or 'lambda'} -> {results}")
