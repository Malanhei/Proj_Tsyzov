'''
 Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Элементы первого файла, отсутствующие во втором:
Элементы второго файла, отсутствующие в первом:
Количество элементов:
Индекс первого минимального элемента:
Индекс последнего максимального элемента:
'''
import random


def create_file(filename, numbers):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, numbers)))


def read_file(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.read().split()))


numbers1 = [random.randint(-100, 100) for _ in range(20)]
numbers2 = [random.randint(-100, 100) for _ in range(20)]

create_file('file1.txt', numbers1)
create_file('file2.txt', numbers2)


nums1 = read_file('file1.txt')
nums2 = read_file('file2.txt')


unique_in_nums1 = set(nums1) - set(nums2)
unique_in_nums2 = set(nums2) - set(nums1)
total_elements = len(nums1) + len(nums2)
min_index = nums1.index(min(nums1))
max_index = nums1.index(max(nums1))


with open('result.txt', 'w') as result_file:
    result_file.write(f"Элементы первого и второго файлов:\n")
    result_file.write(f"Первый файл: {nums1}\n")
    result_file.write(f"Второй файл: {nums2}\n\n")
    
    result_file.write(f"Элементы первого файла, отсутствующие во втором:\n")
    result_file.write(f"{unique_in_nums1}\n\n")
    
    result_file.write(f"Элементы второго файла, отсутствующие в первом:\n")
    result_file.write(f"{unique_in_nums2}\n\n")
    
    result_file.write(f"Количество элементов:\n")
    result_file.write(f"{total_elements}\n\n")
    
    result_file.write(f"Индекс первого минимального элемента:\n")
    result_file.write(f"{min_index}\n\n")
    
    result_file.write(f"Индекс последнего максимального элемента:\n")
    result_file.write(f"{max_index}\n")

print("Файл result.txt успешно создан.")