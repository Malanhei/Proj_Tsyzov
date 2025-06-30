import tkinter as tk
from tkinter import ttk, messagebox
from tracker import (
    add_income,
    add_expense,
    list_transactions,
    delete_transaction,
    get_balance
)
from plotter import plot_income_vs_expense_by_category
from db import init_db
from datetime import datetime

# Инициализация базы данных
init_db()

# Окно
root = tk.Tk()
root.title("Финансовый трекер")
root.geometry("800x650")
root.configure(bg="#f4f4f4")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f4f4f4", font=("Segoe UI", 11))
style.configure("TButton", padding=6, font=("Segoe UI", 10, "bold"))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
style.configure("Treeview", font=("Segoe UI", 10))

# Метка баланса
balance_var = tk.StringVar()

def update_balance():
    balance = get_balance()
    balance_var.set(f"Текущий баланс: {balance:.2f} ₽")

balance_label = ttk.Label(root, textvariable=balance_var, font=("Segoe UI", 12, "bold"), foreground="blue", padding=10)
balance_label.pack()

# Вводная панель
frame = ttk.Frame(root, padding=15)
frame.pack(fill='x', pady=10)

ttk.Label(frame, text="Сумма:").grid(row=0, column=0, sticky="w", padx=5)
amount_entry = ttk.Entry(frame, font=("Segoe UI", 10))
amount_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Категория:").grid(row=1, column=0, sticky="w", padx=5)
category_entry = ttk.Entry(frame, font=("Segoe UI", 10))
category_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Дата(необязательно)):").grid(row=2, column=0, sticky="w", padx=5)
date_entry = ttk.Entry(frame, font=("Segoe UI", 10))
date_entry.grid(row=2, column=1, padx=5, pady=5)

# Функции
def submit_transaction(t_type):
    try:
        amount = float(amount_entry.get())
        category = category_entry.get().strip()
        date = date_entry.get().strip()

        if not category:
            raise ValueError("Категория не указана")

        if not date:
            date = datetime.now().isoformat()

        if t_type == 'Доход':
            add_income(amount, category, date)
        else:
            add_expense(amount, category, date)

        update_transaction_list()

        # Очистка полей
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные данные!")

def update_transaction_list():
    transactions = list_transactions()
    listbox.delete(*listbox.get_children())
    for row in transactions:
        listbox.insert('', 'end', iid=row[0], values=row[1:])
    update_balance()

def show_plot():
    plot_income_vs_expense_by_category()

def delete_selected():
    selected = listbox.selection()
    if not selected:
        messagebox.showwarning("Удаление", "Выберите транзакцию.")
        return
    for item in selected:
        delete_transaction(int(item))
    update_transaction_list()

# Кнопки
button_frame = ttk.Frame(root, padding=10)
button_frame.pack(fill='x')

ttk.Button(button_frame, text="Добавить доход", command=lambda: submit_transaction('Доход')).pack(side='left', padx=10)
ttk.Button(button_frame, text="Добавить расход", command=lambda: submit_transaction('Расход')).pack(side='left', padx=10)
ttk.Button(button_frame, text="Показать график", command=show_plot).pack(side='left', padx=10)
ttk.Button(button_frame, text="Удалить выбранное", command=delete_selected).pack(side='left', padx=10)

# Таблица
table_frame = ttk.Frame(root, padding=10)
table_frame.pack(fill='both', expand=True)

listbox = ttk.Treeview(table_frame, columns=("amount", "type", "category", "date"), show='headings', height=15)
listbox.heading("amount", text="Сумма")
listbox.heading("type", text="Тип")
listbox.heading("category", text="Категория")
listbox.heading("date", text="Дата")
listbox.column("amount", width=100, anchor='center')
listbox.column("type", width=80, anchor='center')
listbox.column("category", width=150, anchor='center')
listbox.column("date", width=220, anchor='center')
listbox.pack(fill='both', expand=True)

# Запуск
update_transaction_list()
root.mainloop()
