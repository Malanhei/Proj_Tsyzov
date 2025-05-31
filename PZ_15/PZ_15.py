import sqlite3


conn = sqlite3.connect("jewelry_workshop.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS izdelie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT NOT NULL,
        master_name TEXT NOT NULL,
        item_type TEXT NOT NULL,
        material TEXT NOT NULL,
        cost REAL NOT NULL
    )
''')


def add_izdelie(client_name, master_name, item_type, material, cost):
    cursor.execute('''
        INSERT INTO izdelie (client_name, master_name, item_type, material, cost)
        VALUES (?, ?, ?, ?, ?)
    ''', (client_name, master_name, item_type, material, cost))
    conn.commit()


def show_all():
    cursor.execute("SELECT * FROM izdelie")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_izdelie(id, client_name, master_name, item_type, material, cost):
    cursor.execute('''
        UPDATE izdelie
        SET client_name = ?, master_name = ?, item_type = ?, material = ?, cost = ?
        WHERE id = ?
    ''', (client_name, master_name, item_type, material, cost, id))
    conn.commit()


def delete_izdelie(id):
    cursor.execute("DELETE FROM izdelie WHERE id = ?", (id,))
    conn.commit()



while True:
    print("\n1. Добавить изделие")
    print("2. Показать все изделия")
    print("3. Изменить изделие")
    print("4. Удалить изделие")
    print("5. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        client = input("ФИО клиента: ")
        master = input("ФИО мастера: ")
        item = input("Вид изделия: ")
        material = input("Материал: ")
        cost = float(input("Стоимость работ: "))
        add_izdelie(client, master, item, material, cost)
        print("Изделие добавлено!\n")

    elif choice == "2":
        print("\nСписок изделий:")
        show_all()

    elif choice == "3":
        id = int(input("ID изделия для изменения: "))
        client = input("Новое ФИО клиента: ")
        master = input("Новое ФИО мастера: ")
        item = input("Новый вид изделия: ")
        material = input("Новый материал: ")
        cost = float(input("Новая стоимость работ: "))
        update_izdelie(id, client, master, item, material, cost)
        print("Изделие обновлено!\n")

    elif choice == "4":
        id = int(input("ID изделия для удаления: "))
        delete_izdelie(id)
        print("Изделие удалено!\n")

    elif choice == "5":
        break

    else:
        print("Неверный выбор, попробуйте снова.")


conn.close()
