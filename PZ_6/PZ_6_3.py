'''
Вар 26
Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
такую точку из данного множества, сумма расстояний от которой до остальных его
точек минимальна, и саму эту сумму

Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
R = sqrt((x2 - x1)**2 + (y2 - y1)**2
R = √(x2 – x1)2 + (у2 – y1)2

Для хранения данных о каждом наборе точек следует использовать по два списка: первый
список для хранения абсцисс, второй — для хранения ординат.

'''
import math

def introduction_int(Content):  # Добавление числа с проверкой
    x = input(Content)
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input(Content)

def read_points():
    N = introduction_int("Введите количество точек (N > 2): ")
    if N <= 2:
        raise ValueError("Количество точек должно быть больше 2.")
    
    x_coords = []
    y_coords = []
    
    for i in range(N):
        x, y = map(float, input(f"Введите координаты точки {i + 1} (x y): ").split())
        x_coords.append(x)
        y_coords.append(y)
    
    return x_coords, y_coords

def calculate_min_distance_point(x_coords, y_coords):
    N = len(x_coords)
    min_distance_sum = float('inf')
    best_point_index = -1
    
    for i in range(N):
        distance_sum = 0
        for j in range(N):
            if i != j:  # Не учитываем расстояние до самой себя
                distance_sum += math.sqrt((x_coords[j] - x_coords[i]) ** 2 + (y_coords[j] - y_coords[i]) ** 2)
        
        if distance_sum < min_distance_sum:
            min_distance_sum = distance_sum
            best_point_index = i
    
    return best_point_index, min_distance_sum


x_coords, y_coords = read_points()
best_point_index, min_distance_sum = calculate_min_distance_point(x_coords, y_coords)

print(f"Точка с индексом {best_point_index + 1} (координаты: ({x_coords[best_point_index]}, {y_coords[best_point_index]})) имеет минимальную сумму расстояний: {min_distance_sum}")
