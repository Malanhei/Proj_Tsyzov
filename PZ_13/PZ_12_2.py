'''
Вар 26
В двумерном списке элементы первого столбца возвести в куб.
'''
import random

def list_generator(x):
    a = []
    for i in range(x):
        a.append(random.randint(-100, 100))
    return a

def return_all(matrix):
    return [[x[0] ** 2] + x[1:] for x in matrix]

general_list = []
for i in range(random.randint(2, 10)):
    general_list.append(list_generator(random.randint(2, 5)))

print("Исходный список:")
print(general_list)

print("\nСписок после обработки:")
print(return_all(general_list))