#Вариант 26
a = int(input('Введите целое число обозначающее сторону a: '))
b = int(input('Введите целое число обозначающее сторону b: '))
c = int(input('Введите целое число обозначающее сторону c: '))

if a+b > c and b+c > a and a+c > b: #сумма двух сторон треугольника должна быть больше третьей стороны
    print('Существует треугольник со сторонами', a, b, c)
else:
    print('Не существует треугольник со сторонами', a, b, c)