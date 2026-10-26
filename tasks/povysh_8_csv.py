"""Задание 8 (повышенной сложности): фильтрация и преобразование CSV
через map/filter.

Обрабатывается CSV-файл с колонками name, group, score:
- filter оставляет записи с баллом не ниже min_score (по умолчанию 60);
- map преобразует запись: балл приводится к числу и добавляется
  поле status со значением «зачёт».

Используется модуль csv (DictReader/DictWriter), файлы читаются
и записываются в UTF-8 с newline="". Входной файл не перезаписывается:
результат пишется в отдельный выходной файл.
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def process_csv(source: str, destination: str, min_score: int = 60) -> int:
    """Фильтрует и преобразует записи CSV.

    Возвращает количество записей, прошедших фильтр.
    """
    with open(source, encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = list(reader.fieldnames or []) + ["status"]
        # filter: только записи с баллом >= min_score
        passed = filter(lambda row: int(row["score"]) >= min_score, reader)
        # map: числовой балл + поле status
        transformed = map(
            lambda row: {**row, "score": int(row["score"]), "status": "зачёт"},
            passed,
        )
        with open(destination, "w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transformed)
    return count_rows(destination)


def count_rows(path: str) -> int:
    """Возвращает количество строк данных (без заголовка) в CSV."""
    with open(path, encoding="utf-8", newline="") as infile:
        return sum(1 for _ in csv.DictReader(infile))


if __name__ == "__main__":
    source = os.path.join(BASE_DIR, "data", "students.csv")
    destination = os.path.join(BASE_DIR, "data", "students_passed.csv")
    written = process_csv(source, destination, min_score=60)
    print(f"Обработано записей: {written}")
    print("Результат записан в", destination)
    with open(destination, encoding="utf-8", newline="") as outfile:
        print(outfile.read())
