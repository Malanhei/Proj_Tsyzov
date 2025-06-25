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
root.geometry("400x390")

# Заголовок формы
tk.Label(root, text="Форма заявки",
         bg="green", fg="white",
         font=("Arial", 12, "bold"),
         highlightbackground="skyblue", highlightthickness=1
).pack(side="top", fill=tk.BOTH)

# Шрифты
bold_font = tkFont.Font(family="Arial", size=9, weight="bold")
normal_font = tkFont.Font(family="Arial", size=9)

# Обёртка для всех секций
frames1 = tk.Frame(root, highlightbackground="skyblue", highlightthickness=1)
frames1.pack(side="top", fill=tk.BOTH)

#1
frame1 = tk.Frame(frames1)
frame1.pack(anchor="w")
tk.Label(frame1, text="Допустимые типы вложений:", font=bold_font).pack(side="left")
tk.Label(frame1, text=" zip, rar, txt, doc, jpg, png, gif, odt, xml", font=normal_font).pack(side="left")

frame2 = tk.Frame(frames1)
frame2.pack(anchor="w", pady=2)
tk.Label(frame2, text="Макс. размер каждого файла:", font=bold_font).pack(side="left")
tk.Label(frame2, text=" 1024kb.", font=normal_font).pack(side="left")

frame3 = tk.Frame(frames1)
frame3.pack(anchor="w", pady=2)
tk.Label(frame3, text="Макс. общий размер файла:", font=bold_font).pack(side="left")
tk.Label(frame3, text=" 2048kb.", font=normal_font).pack(side="left")

#2
frames2 = tk.Frame(root)
frames2.pack(side="top", fill=tk.BOTH)

frame21 = tk.Frame(frames2, highlightbackground="skyblue", highlightthickness=1, width=150, height=25)
frame21.pack_propagate(False)
frame21.pack(side="left")
tk.Label(frame21, text="Ваше имя:", font=normal_font).pack(side="left")

frame22 = tk.Frame(frames2, highlightbackground="skyblue", highlightthickness=1, width=250, height=25)
frame22.pack_propagate(False)
frame22.pack(side="left")
name_entry = tk.Entry(frame22, width=30)
name_entry.pack(side="left", padx=2, pady=2)
tk.Label(frame22, text="*", font=normal_font, fg='red').pack(side="left")

#3 
frames3 = tk.Frame(root)
frames3.pack(side="top", fill=tk.BOTH)

frame31 = tk.Frame(frames3, highlightbackground="skyblue", highlightthickness=1, width=150, height=25)
frame31.pack_propagate(False)
frame31.pack(side="left")
tk.Label(frame31, text="Ваш Email:", font=normal_font).pack(side="left")

frame32 = tk.Frame(frames3, highlightbackground="skyblue", highlightthickness=1, width=250, height=25)
frame32.pack_propagate(False)
frame32.pack(side="left")
email_entry = tk.Entry(frame32, width=30)
email_entry.pack(side="left", padx=2, pady=2)
tk.Label(frame32, text="*", font=normal_font, fg='red').pack(side="left")

#4
frames4 = tk.Frame(root)
frames4.pack(side="top", fill=tk.BOTH)

frame41 = tk.Frame(frames4, highlightbackground="skyblue", highlightthickness=1, width=150, height=25)
frame41.pack_propagate(False)
frame41.pack(side="left")
tk.Label(frame41, text="Тема письма:", font=normal_font).pack(side="left")

frame42 = tk.Frame(frames4, highlightbackground="skyblue", highlightthickness=1, width=250, height=25)
frame42.pack_propagate(False)
frame42.pack(side="left")
subject_entry = tk.Entry(frame42, width=30)
subject_entry.pack(side="left", padx=2, pady=2)

#5-7
file_entries = []
for i in range(3):
    i = tk.Frame(root)
    i.pack(side="top", fill=tk.BOTH)
    framei1 = tk.Frame(i, highlightbackground="skyblue", highlightthickness=1, width=150, height=25)
    framei1.pack_propagate(False)
    framei1.pack(side="left")
    tk.Label(framei1, text="Прикрепить файл:", font=normal_font).pack(side="left")

    framei2 = tk.Frame(i, highlightbackground="skyblue", highlightthickness=1, width=250, height=25)
    framei2.pack_propagate(False)
    framei2.pack(side="left")
    file_entry = tk.Entry(framei2, width=30)
    file_entry.pack(side="left", padx=2, pady=2)
    file_entries.append(file_entry)

    tk.Button(framei2, text="Обзор...", command=lambda e=file_entry: browse_file(e)).pack(side="left", padx=2, pady=2)

#8
frames8 = tk.Frame(root, highlightbackground="skyblue", highlightthickness=1)
frames8.pack(side="top", fill=tk.BOTH)

frame81 = tk.Frame(frames8)
frame81.pack(anchor='nw')
tk.Label(frame81, text="Ваше сообщение:", font=normal_font).pack(side="left")
tk.Label(frame81, text="*", font=normal_font, fg='red').pack(side="left")

frame82 = tk.Frame(frames8, highlightbackground="skyblue", highlightthickness=1, width=350, height=100)
message_text = tk.Text(frame82, width=40, height=5)
message_text.pack(side="bottom")
frame82.pack(side="bottom")

#9
frames9 = tk.Frame(root, background='green')
frames9.pack(side="top", fill=tk.BOTH)

frame91 = tk.Frame(frames9, background='green')
frame91.pack(anchor="center")
tk.Button(frame91, text="Отправить Email", command=submit_form).pack(side='left', padx=5, pady=3)
tk.Button(frame91, text="Очистить", command=clear_form).pack(side="left", padx=5, pady=3)

root.mainloop()