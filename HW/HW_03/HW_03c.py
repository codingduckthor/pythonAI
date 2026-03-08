# Файл data/students.csv содержит столбцы name, age, grade.
# Нужно:
# 1) прочитать CSV
# 2) выбрать студентов с grade >= 85
# 3) записать их в data/good_students.csv с теми же заголовками
# 4) дополнительно вывести: сколько всего было и сколько осталось после фильтра
#
# Критерии оценки
# •	программа запускается без ошибок и читает файлы из папки data/;
# •	правильно использован with open(...);
# •	есть обработка пустых строк (strip + continue);
# •	отчет сохранен в файл в требуемом формате; • для CSV корректно приведены типы (int/float).


import csv

total_students = 0
good_students = 0

with open("data/students.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    students = []

    for row in reader:
        if not row["name"].strip():
            continue

        total_students += 1

        grade = float(row["grade"])

        if grade >= 85:
            students.append(row)
            good_students += 1


with open("data/good_students.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)


print("Students total:", total_students)
print("Students with grade over 85:", good_students)
