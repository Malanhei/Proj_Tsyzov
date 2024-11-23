'''
Вар 26
Составить программу, в которой функцию построит изображение, в котором в
первой строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m
звездочек.
'''
def proverka_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

m = input('Введите кол-во строчек: ')
m = proverka_int(m)

while m < 0:
    print('m должно быть больше 0!')
    m = input('Введите кол-во строчек: ')
    m = proverka_int(m)

for i in range(1, m + 1):
    star = '*'
    print(star * i)
