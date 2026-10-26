"""Тесты задания 1 (повышенной сложности): композиция функций."""

import unittest

from tasks.povysh_1_compose import compose


class ComposeTest(unittest.TestCase):
    def test_right_to_left_order(self):
        # compose(double, add_three)(4) == double(add_three(4)) == 14
        combined = compose(lambda x: x * 2, lambda x: x + 3)
        self.assertEqual(combined(4), 14)

    def test_three_functions(self):
        # ((4 + 3) * 2) - 1 = 13
        combined = compose(
            lambda x: x - 1,
            lambda x: x * 2,
            lambda x: x + 3,
        )
        self.assertEqual(combined(4), 13)

    def test_single_function(self):
        combined = compose(lambda x: x + 1)
        self.assertEqual(combined(10), 11)

    def test_empty_compose_is_identity(self):
        identity = compose()
        self.assertEqual(identity(42), 42)
        self.assertEqual(identity("текст"), "текст")

    def test_string_pipeline(self):
        pipeline = compose(str.strip, str.lower)
        self.assertEqual(pipeline("  ПРИВЕТ  "), "привет")


if __name__ == "__main__":
    unittest.main()
