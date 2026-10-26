"""Тесты задания 8 (средней сложности): декоратор замера времени."""

import unittest
from unittest import mock

from tasks.sredn_8_timer import measure_time


class MeasureTimeTest(unittest.TestCase):
    def test_returns_result_and_passes_arguments(self):
        @measure_time
        def add(a, b, coefficient=1):
            """Складывает числа."""
            return (a + b) * coefficient

        self.assertEqual(add(2, 3, coefficient=2), 10)

    def test_wraps_preserves_metadata(self):
        @measure_time
        def example():
            """Документация."""

        self.assertEqual(example.__name__, "example")
        self.assertEqual(example.__doc__, "Документация.")

    def test_duration_measured(self):
        @measure_time
        def work():
            return 42

        work()
        self.assertIsNotNone(work.last_duration)
        self.assertGreaterEqual(work.last_duration, 0)

    def test_exception_is_propagated_and_time_measured(self):
        @measure_time
        def failing():
            raise ValueError("ошибка")

        with self.assertRaises(ValueError):
            failing()
        self.assertIsNotNone(failing.last_duration)

    def test_duration_value_with_mocked_clock(self):
        with mock.patch("tasks.sredn_8_timer.time.perf_counter",
                        side_effect=[10.0, 12.5]):
            @measure_time
            def work():
                return 1

            work()
        self.assertAlmostEqual(work.last_duration, 2.5)


if __name__ == "__main__":
    unittest.main()
