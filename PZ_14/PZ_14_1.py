'''
В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
Достоевского (т.е. с различными окончаниями, например, Достоевский,
Достоевского) в единственном экземпляре.
'''
import re


with open("Dostoevsky.txt", "r", encoding="utf-8") as file:
    text = file.read()


matches = re.findall(r"\bДостоевск\w*\b", text)


unique_matches = set(matches)


for match in sorted(unique_matches):
    print(match)
