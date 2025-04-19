'''
Составить генератор (yield), который выводит из строки только буквы
'''
from string import ascii_letters

def letters_generator(input_string):
    for char in input_string:
        if char in ascii_letters: 
            yield char


input_string = "Hello, World! 123"
print(f"Исходная строка: {input_string}")


print("Буквы из строки:")
for i in letters_generator(input_string):
    print(i, end=" ")  
