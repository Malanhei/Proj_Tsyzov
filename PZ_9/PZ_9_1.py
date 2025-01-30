'''
Вариант 26
Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
средние температуры по месяцам в году. Преобразовать информацию из строки в
словарь, с использованием функции найти среднюю и минимальные температуры,
результаты вывести на экран.
'''

string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

parts = string.split()

year = parts[0]

temperatures = list(map(int, parts[1:]))

mounths = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
            'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

main_dict = {mounths[i]: temperatures[i] for i in range(len(mounths))}

def calculate_average(x):
    return sum(x.values()) / len(x)


def min_temp(x):
    return min(x)

for i, b in main_dict.items():
    print(f'{i}: {b}')

print('Средняя температура за год:', round(calculate_average(main_dict), 3))
print('Минимальная температура за год:', main_dict[min_temp(main_dict)])