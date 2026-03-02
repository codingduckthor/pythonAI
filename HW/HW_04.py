import numpy as np

#1. Сгенерируйте 20 случайных целых чисел от 0 до 100. Выведите: mean, min, max, std (np.std)

arr1 = np.random.randint(0, 101, 20) # заполняем массив числами от 0 до 100 двадцатью случайно выбранными числами

print("сам массив:", arr1)
print("среднее значение:", arr1.mean())
print("минимальное значение:", arr1.min())
print("максимальное:", arr1.max())
print("отклонение:", np.std(arr1))


#2. Создайте массив [1..30]. Оставьте только числа, которые делятся на 3 (используйте условие).

arr2 = np.arange(1, 31) # заполняем массив от 1 до 30
result = arr2[arr2 % 3 == 0] # новый массив, заполненный числами из первого массива, которые делятся на 3

print(arr2)
print(result)


#3. Дан массив: [3, 10, 5, 8, 2, 7]. Замените все элементы меньше 6 на 0 (np.where)

arr3 = np.array([3, 10, 5, 8, 2, 7])

status = np.where(arr3 < 6, 0, arr3) # если число меньше 6, то добавляем его в новый массив
print(status)


#4. Создайте матрицу 5x5 из случайных целых 1..9. Найдите: сумму по строкам, сумму по столбцам, сумму главной диагонали (np.trace)

matrix = np.random.randint(low=1, high=10, size=(5, 5))
print(matrix)

sum_rows = matrix.sum(axis=1)
print("сумма по строкам:", sum_rows)

sum_cols = matrix.sum(axis=0)
print("сумма по столбцам:", sum_cols)

sum_diag = np.trace(matrix)
print("сумма по диагонали:", sum_diag)


#5. Дана матрица оценок 4x3 (4 студента, 3 теста). Посчитайте средний балл каждого студента (axis=1) и каждого теста (axis=0

np.random.seed(42)
grades = np.random.randint(low=0, high=6, size=(4, 3))

avr_grade1 = grades.mean(axis=1)

avr_grade2 = grades.mean(axis=0)

print("оценки и тесты:\n", grades)
print("средний балл каждого студента:", avr_grade1)
print("средний балл каждого теста:", avr_grade2)


#6 Дан массив температур за 7 дней (вы придумайте сами). Найдите индексы дней, когда температура выше среднего (np.where).

temps = np.array([5.3, 6.4, 3.0, 2.8, 10, 8, 8.4]) # это массив температур за 7 дней

avr = temps.mean() # это средняя температура за 7 дней
print(avr)

days = np.where(temps > avr)
print("индексы дней с температурой выше среднего:", days[0])

#7 Нормализуйте температуры в диапазон 0..1 по формуле (x-min)/(max-min)

temps_norm = (temps - temps.min()) / (temps.max() - temps.min())
print("нормализованные температуры (0..1):", temps_norm)

#8 Ограничьте температуры снизу 0 и сверху 40 (np.clip), объясните зачем это может быть нужно

temps_clipped = np.clip(temps, 0, 40)
print("ограниченные температуры (0..40):", temps_clipped)
