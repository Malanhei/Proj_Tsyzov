'''
вар 26
Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
расположенные между A и B (не включая числа A и B), а также количество N этих
чисел.

'''
a = input('Введите a ')
while type(a) != int:   #Проверка числа
    try:
        a = int(a)
    except:
        print('Неправильно ввели')
        a = input('Введите a ')

b = input('Введите b ')
while type(b) != int:    #Проверка числа
    try:
        b = int(b)
    except:
        print('Неправильно ввели')
        b = input('Введите b ')

while a > b:           #Проверка: a < b
    print('a длжно быть меньше b')
    a = input('Введите a ')
    while type(a) != int:   #Проверка числа
        try:
            a = int(a)
        except:
            print('Неправильно ввели')
            a = input('Введите a ')
    b = input('Введите b ')
    while type(b) != int:    #Проверка числа
        try:
            b = int(b)
        except:
            print('Неправильно ввели')
            b = input('Введите b ')



k = 0

for i in range(b, a - 1, -1):
    k += 1
    print(i, end=' ')
print('\n', 'Кол-во чисел ', k, sep='')