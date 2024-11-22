'''
Вар 26
 Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем
положительные и отрицательные числа. Если чередуются, то вывести 0, если нет, то
вывести порядковый номер первого элемента, нарушающего закономерность.
'''
ListAppend = []


def introduction_int(Content):  # Добавление числа с проверкой
    x = input(Content)
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input(Content)


def alternation(List): # Узнаём идёт чередование или нет
    for i in range(1, element):
        if (List[i] > 0 and List[i - 1] > 0) or (List[i] < 0 and List[i - 1] < 0):
            return i + 1
    return 0


element = introduction_int('Введите сколько будет элемнтов списка: ')

for i in range(element):
    ListAppend.append(introduction_int(f'Введите {i + 1} элемент списка '))

print(alternation(ListAppend))
    