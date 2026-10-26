"""Тесты задания 8 (повышенной сложности): фильтрация и преобразование CSV."""

import csv
import os
import tempfile
import unittest

from tasks.povysh_8_csv import process_csv

CSV_CONTENT = (
    "name,group,score\n"
    "Иванов Иван,221141,45\n"
    "Петров Пётр,221141,72\n"
    "Сидоров Сидор,221142,60\n"
    "Кузнецова Анна,221142,95\n"
    "Смирнов Олег,221141,59\n"
    '"Студент с, запятой в имени",221141,66\n'
)


def write_csv(directory, content=CSV_CONTENT):
    path = os.path.join(directory, "input.csv")
    with open(path, "w", encoding="utf-8", newline="") as file:
        file.write(content)
    return path


def read_rows(path):
    with open(path, encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


class CsvProcessingTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.source = write_csv(self.tmp.name)
        self.destination = os.path.join(self.tmp.name, "output.csv")

    def tearDown(self):
        self.tmp.cleanup()

    def test_filter_and_transform(self):
        written = process_csv(self.source, self.destination, min_score=60)
        self.assertEqual(written, 4)
        rows = read_rows(self.destination)
        self.assertEqual(len(rows), 4)
        # исключены баллы 45 и 59, граничный 60 оставлен
        self.assertEqual(
            [row["name"] for row in rows],
            ["Петров Пётр", "Сидоров Сидор", "Кузнецова Анна",
             "Студент с, запятой в имени"],
        )
        for row in rows:
            self.assertEqual(row["status"], "зачёт")
            self.assertEqual(row["score"], str(int(row["score"])))

    def test_boundary_score_included(self):
        written = process_csv(self.source, self.destination, min_score=95)
        rows = read_rows(self.destination)
        self.assertEqual(written, 1)
        self.assertEqual(rows[0]["name"], "Кузнецова Анна")

    def test_no_matches_keeps_header(self):
        written = process_csv(self.source, self.destination, min_score=1000)
        self.assertEqual(written, 0)
        with open(self.destination, encoding="utf-8", newline="") as file:
            first_line = file.readline().strip()
        self.assertEqual(first_line, "name,group,score,status")

    def test_cyrillic_and_quoted_comma(self):
        written = process_csv(self.source, self.destination, min_score=66)
        rows = read_rows(self.destination)
        self.assertEqual(written, 3)
        self.assertIn("Студент с, запятой в имени", [row["name"] for row in rows])

    def test_score_converted_to_int_in_output(self):
        process_csv(self.source, self.destination, min_score=60)
        rows = read_rows(self.destination)
        for row in rows:
            self.assertTrue(row["score"].isdigit())

    def test_source_not_modified(self):
        with open(self.source, encoding="utf-8", newline="") as file:
            before = file.read()
        process_csv(self.source, self.destination, min_score=60)
        with open(self.source, encoding="utf-8", newline="") as file:
            after = file.read()
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
