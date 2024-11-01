'''
Вар 26
Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
положительного числа K на обратный (K — параметр целого типа, являющийся
одновременно входным и выходным). С помощью этой функции поменять порядок
следования цифр на обратный для каждого из пяти данных целых чисел.

'''
def proverka_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')


def InvertDigits(k):
    f = ''
    while k > 0:
        digit = k % 10
        k = k // 10
        f = f + str(digit)
    return int(f)



t = input('Введите число: ')
t = proverka_int(t)
if t < 0:
    t = t * (-1)
    print(InvertDigits(t) * (-1))
else:
    print(InvertDigits(t))