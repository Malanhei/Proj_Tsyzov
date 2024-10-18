'''
Вар 26
Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.
'''

n = input('Введите n ')
while type(n) != int:   #Проверка числа
    try:
        n = int(n)
    except:
        print('Неправильно ввели')
        n = input('Введите n ')

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



