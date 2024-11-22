'''
Вар 26
Дан целочисленный список A размера N (< 15). Переписать в новый целочисленный
список B все элементы с нечетными порядковыми номерами (1,3,...) и вывести
размер полученного списка B и его содержимое. Условный оператор не
использовать.

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

while True:
    element = introduction_int('Введите сколько будет элемнтов списка(<15): ')
    if element < 15:
        break
    else:
        print('Слишком много элемнтов списка')

for i in range(element):
    ListAppend.append(introduction_int(f'Введите {i + 1} элемент списка '))

b = []

for i in range(0, element, 2):
    b.append(ListAppend[i])

print(b, len(b))