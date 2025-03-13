'''
В последовательности их N чисел (N –четное) во второй ее половине найти сумму
элементов больших 10
'''
from functools import reduce

# Исходная последовательность чисел (N — четное)
numbers = [5, 12, 3, 8, 15, 7, 20, 11]

# Длина последовательности
N = len(numbers)

# Разделяем последовательность на две половины
first_half = numbers[:N//2]
second_half = numbers[N//2:]

# Фильтруем элементы второй половины, которые больше 10
filtered_numbers = filter(lambda x: x > 10, second_half)

# Суммируем отфильтрованные элементы
sum_greater_than_10 = reduce(lambda x, y: x + y, filtered_numbers)

print(f"Сумма элементов второй половины, больших 10: {sum_greater_than_10}")