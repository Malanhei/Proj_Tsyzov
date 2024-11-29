'''
Вар 26
Даны целые положительные числа N1 и N2 и строки S1 и S2. Получить из этих строк
новую строку, содержащую первые N1 символов строки S1 и последние N2
символов строки S2 (в указанном порядке). 
'''

def introduction_int(Content):  # Добавление числа с проверкой
    x = input(Content)
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно ')
            x = input(Content)


while True:
    n1 = introduction_int('Введите N1 ')
    s1 = input('Введите S1 ')
    if len(s1) > n1:
        break
    else:
        print("N1 должго быть меньше S1 ")

while True:
    n2 = introduction_int('Введите N2 ')
    s2 = input('Введите S2 ')
    if len(s2) > n2:
        break
    else:
        print("N2 должго быть меньше S2 ")

new_str = (s1[:n1] + s2[-n2:]) 
print(new_str)