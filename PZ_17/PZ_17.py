import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkFont

# Функция обработки нажатия кнопки Обзор
def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# Функция для кнопки Отправить Email
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    message = message_text.get("1.0", tk.END)
    if not name or not email or not message.strip():
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните обязательные поля.")
    else:
        messagebox.showinfo("Отправлено", "Форма успешно отправлена!")

# Функция для кнопки Очистить
def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    for entry in file_entries:
        entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Форма заявки")


root.geometry("400x430")

# Центрирование по 3 колонкам
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# Заголовок формы (верхняя часть, row=0)
tk.Label(root, text="Форма заявки", 
         bg="green", fg="black", font=("Arial", 12, "bold"), highlightbackground="skyblue", highlightthickness=2
).grid(row=0, column=0, columnspan=3, sticky="nsew", pady=10)

# Шрифты
bold_font = tkFont.Font(family="Arial", size=9, weight="bold")
normal_font = tkFont.Font(family="Arial", size=9)

# Первая строка (перенесли на row=1)
frame1 = tk.Frame(root)
frame1.grid(row=1, column=0, columnspan=3, sticky="w")
tk.Label(frame1, text="Допустимые типы вложений:", font=bold_font).pack(side="left")
tk.Label(frame1, text=" zip, rar, txt, doc, jpg, png, gif, odt, xml", font=normal_font).pack(side="left")

# Вторая строка
frame2 = tk.Frame(root)
frame2.grid(row=2, column=0, columnspan=3, sticky="w")
tk.Label(frame2, text="Макс. размер каждого файла:", font=bold_font).pack(side="left")
tk.Label(frame2, text=" 1024kb.", font=normal_font).pack(side="left")

# Третья строка
frame3 = tk.Frame(root)
frame3.grid(row=3, column=0, columnspan=3, sticky="w")
tk.Label(frame3, text="Макс. общий размер файла:", font=bold_font).pack(side="left")
tk.Label(frame3, text=" 2048kb.", font=normal_font).pack(side="left")

# Полоска-разделитель
tk.Frame(root, height=1, bg="gray", bd=0).grid(row=4, column=0, columnspan=3, sticky="we", pady=5)

tk.Label(root, text="Ваше имя:*").grid(row=5, column=0, sticky="e")
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=5, column=1)

tk.Label(root, text="Ваш Email:*").grid(row=6, column=0, sticky="e")
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=6, column=1)

# Полоска-разделитель
tk.Frame(root, height=1, bg="gray", bd=0).grid(row=7, column=0, columnspan=3, sticky="we", pady=5)

tk.Label(root, text="Тема письма:").grid(row=8, column=0, sticky="e")
subject_entry = tk.Entry(root, width=40)
subject_entry.grid(row=8, column=1)

# Полоска-разделитель
tk.Frame(root, height=1, bg="gray", bd=0).grid(row=9, column=0, columnspan=3, sticky="we", pady=5)

# Прикрепленные файлы
file_entries = []
for i in range(3):
    tk.Label(root, text="Прикрепить файл:").grid(row=10+i, column=0, sticky="e")
    file_entry = tk.Entry(root, width=30)
    file_entry.grid(row=10+i, column=1)
    file_entries.append(file_entry)
    tk.Button(root, text="Обзор...", command=lambda e=file_entry: browse_file(e)).grid(row=10+i, column=2)

# Полоска-разделитель
tk.Frame(root, height=1, bg="gray", bd=0).grid(row=13, column=0, columnspan=3, sticky="we", pady=5)

tk.Label(root, text="Ваше сообщение:*").grid(row=14, column=0, sticky="ne")
message_text = tk.Text(root, width=40, height=5)
message_text.grid(row=14, column=1, columnspan=2)

# Полоска-разделитель
tk.Frame(root, height=1, bg="gray", bd=0).grid(row=15, column=0, columnspan=3, sticky="we", pady=5)

tk.Button(root, text="Отправить Email", command=submit_form).grid(row=16, column=1, sticky="e")
tk.Button(root, text="Очистить", command=clear_form).grid(row=16, column=2, sticky="w")

root.mainloop()
