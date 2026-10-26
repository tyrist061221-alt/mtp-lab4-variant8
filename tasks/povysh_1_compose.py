"""Задание 1 (повышенной сложности): композиция функций (compose).

compose(f, g)(x) == f(g(x)) — функции применяются справа налево.
Композиция из одной функции равна самой функции, композиция без
функций — тождественная функция.
"""


def compose(*functions):
    """Возвращает композицию унарных функций.

    compose(f, g, h)(x) == f(g(h(x))).
    """
    def composed(value):
        result = value
        for function in reversed(functions):
            result = function(result)
        return result

    return composed


if __name__ == "__main__":
    # порядок важен: (x + 3) применяется первым, затем * 2
    add_three = lambda x: x + 3        # noqa: E731
    double = lambda x: x * 2            # noqa: E731
    combined = compose(double, add_three)
    print("compose(double, add_three)(4) =", combined(4), "(= double(add_three(4)))")

    text_pipeline = compose(
        str.strip,
        lambda s: s.lower(),
        lambda s: s.replace("  ", " "),
    )
    print("Обработка строки:", text_pipeline("  Привет   Мир  "))
