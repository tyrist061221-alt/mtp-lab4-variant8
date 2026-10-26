"""Тесты задания 10 (средней сложности): несколько функций через map."""

import unittest

from tasks.sredn_10_multi_map import apply_functions


class ApplyFunctionsTest(unittest.TestCase):
    def test_two_functions(self):
        result = apply_functions(
            [1, 2, 3],
            [lambda x: x ** 2, lambda x: x + 1],
        )
        self.assertEqual(result, [[1, 4, 9], [2, 3, 4]])

    def test_single_function(self):
        result = apply_functions([1, 2], [lambda x: x * 10])
        self.assertEqual(result, [[10, 20]])

    def test_empty_values(self):
        result = apply_functions([], [lambda x: x + 1])
        self.assertEqual(result, [[]])

    def test_empty_functions(self):
        self.assertEqual(apply_functions([1, 2], []), [])

    def test_both_empty(self):
        self.assertEqual(apply_functions([], []), [])


if __name__ == "__main__":
    unittest.main()
