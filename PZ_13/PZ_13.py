from functools import reduce

# Исходная матрица
matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [-7, 8, 9]
]


# Преобразуем в одномерный список
all_elements = reduce(lambda a, b: a + b, matrix)
# Фильтруем только положительные
positive_elements = list(filter(lambda x: x > 0, all_elements))
# Считаем среднее
average = sum(positive_elements) / len(positive_elements) if positive_elements else 0

print("Среднее арифметическое положительных элементов:", average)


# Возводим в куб элементы первого столбца с помощью list comprehension
cubed_matrix = [[row[0] ** 3] + row[1:] for row in matrix]

print("Матрица с кубами в первом столбце:")
for row in cubed_matrix:
    print(row)
