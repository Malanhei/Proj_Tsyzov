'''
вар 26
Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
расположенные между A и B (не включая числа A и B), а также количество N этих
чисел.

'''
def proverka_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

a = input('Введите a ')
a = proverka_int(a)

b = input('Введите b ')
b = proverka_int(b)

while a > b:           #Проверка: a < b
    print('a длжно быть меньше b')
    a = input('Введите a ')
    a = proverka_int(a)
    
    b = input('Введите b ')
    b = proverka_int(b)



k = 0

for i in range(b, a - 1, -1):
    k += 1
    print(i, end=' ')
print('\n', 'Кол-во чисел ', k, sep='')