'''
Из предложенного текстового файла (text18-26.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно заменив все знаки пунктуации на знак «/».
'''
import string


def count_punctuation(text):
    return sum(1 for char in text if char in string.punctuation)


def replace_punctuation(text):
    return ''.join(['/' if char in string.punctuation else char for char in text])


with open('text18-26.txt', 'r', encoding='UTF-16') as file:
    content = file.read()


print("Содержимое файла:")
print(content)


punctuation_count = count_punctuation(content)
print(f"\nКоличество знаков препинания: {punctuation_count}")


modified_content = replace_punctuation(content)


with open('modified_text.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(modified_content)

print("\nТекст с замененными знаками препинания сохранен в файл 'modified_text.txt'.")