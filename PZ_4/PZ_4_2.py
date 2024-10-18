'''
Вар 26
Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.
'''
def proverka_int(x):    #Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

n = input('Введите n ')
n = proverka_int(n)

k = 1
total_sum = 0
while True:
    total_sum += k
    if total_sum == n:
        k += 1
        break
    elif total_sum < n:
        k += 1
    elif total_sum > n:
        total_sum -= k
        break
print('Наибольшее кол-во k =', k-1, 'а сумма =', total_sum)



