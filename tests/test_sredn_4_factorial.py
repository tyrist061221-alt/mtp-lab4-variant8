"""Тесты задания 4 (средней сложности): факториал через reduce."""

import math
import unittest

from tasks.sredn_4_factorial import factorial


class FactorialTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_known_values(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_matches_math_factorial(self):
        for n in range(0, 12):
            self.assertEqual(factorial(n), math.factorial(n))

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_non_integer_raises(self):
        with self.assertRaises(TypeError):
            factorial(2.5)
        with self.assertRaises(TypeError):
            factorial("5")


if __name__ == "__main__":
    unittest.main()
