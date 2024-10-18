'''
вар 26
Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
лежит в четвертой координатной четверти»
'''
def proverka_float(x):
    while type(x) != float:
        try:
            x = float(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

x = input('Введите кооардинату x: ')
x = proverka_float(x)
y = input('Введите кооардинату y: ')
y = proverka_float(y)

if x>0 and y<0:
    print("Точка лежит в четвертой координатной четверти")
else:
    print("Точка не лежит в четвертой координатной четверти")