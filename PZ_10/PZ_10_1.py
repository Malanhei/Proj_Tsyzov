'''
Вариант 26:
Книжные магазины предлагают следующие коллекции книг.
Мансистр – Лермонтов, Достоевский, Пушкин, Тютчев
Домбинич – Толстой, Грибоедов, Чехов, Пушкин,
Бумбаркет – Пушкин, Достоевский, Маяковский,
Галерея – Чехов, Тютчев, Пушкин, Определить:
1. Полный список всех книг магазинов.
2. Какие книги есть во всех магазинах.
3. Хотя бы одну книгу, которая есть не во всех магазинах.
'''
'''
books = {
    "Мансистр": ["Лермонтов", "Достоевский", "Пушкин", "Тютчев"],
    "Домбинич": ["Толстой", "Грибоедов", "Чехов", "Пушкин"],
    "Бумбаркет": ["Пушкин", "Достоевский", "Маяковский"],
    "Галерея": ["Чехов", "Тютчев", "Пушкин"]
}

def all_books(books):
    b = set()
    for collection in books.values():
        for book in collection:
            b.add(book)
    return list(b)

def books_all_store(books):
    sets = []
    for collection in books.values():
        sets.append(set(collection))
    return list(set.intersection(*sets))

def book(books):
    all_books_set = all_books(books)
    common_books = books_all_store(books)
    for i in common_books:
        all_books_set.remove(i)

    return all_books_set
'''

manistr = ("Лермонтов", "Достоевский", "Пушкин", "Тютчев")
dombinich = ("Толстой", "Грибоедов", "Чехов", "Пушкин")
bumbarket = ("Пушкин", "Достоевский", "Маяковский")
galereya = ("Чехов", "Тютчев", "Пушкин")



# Вывод результатов
print(f"1. Список всех книг: {set(manistr + dombinich + bumbarket + galereya)}")

print(f"2. Книги, которые есть во всех магазинах: {set(manistr) & set(dombinich) & set(bumbarket) & set(galereya)}")

print(f"3. Книги, которые есть не во всех магазинах: {(set(manistr + dombinich + bumbarket + galereya)) - (set(manistr) & set(dombinich) & set(bumbarket) & set(galereya))}")
