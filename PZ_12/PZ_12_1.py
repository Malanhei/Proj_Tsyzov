'''
В последовательности их N чисел (N –четное) во второй ее половине найти сумму
элементов больших 10
'''
from functools import reduce

numbers = [5, 12, 3, 8, 15, 7, 20, 11]

N = len(numbers)

second_half = numbers[N//2:]

filtered_numbers = filter(lambda x: x > 10, second_half)

sum_greater_than_10 = reduce(lambda x, y: x + y, filtered_numbers)

print(f"Сумма элементов второй половины, больших 10: {sum_greater_than_10}")