import tkinter as tk

# Создаем основное окно
root = tk.Tk()
root.title("Библиотечная информационная система")

# Создаем базовую базу данных книг
library_books = []

# Создаем функции для добавления, бронирования и удаления книг
def add_book():
    book_title = title_entry.get()
    book_author = author_entry.get()
    library_books.append({"title": book_title, "author": book_author, "available": True})
    update_book_list()

def reserve_book():
    selected_index = book_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        library_books[selected_index]["available"] = False
        update_book_list()

def delete_book():
    selected_index = book_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del library_books[selected_index]
        update_book_list()

def update_book_list():
    book_listbox.delete(0, tk.END)
    for book in library_books:
        status = "Доступна" if book["available"] else "Забронирована"
        book_listbox.insert(tk.END, f"{book['title']} by {book['author']} - {status}")

# Создаем интерфейс для добавления книг
add_label = tk.Label(root, text="Добавить книгу")
title_label = tk.Label(root, text="Название:")
author_label = tk.Label(root, text="Автор:")
title_entry = tk.Entry(root)
author_entry = tk.Entry(root)
add_button = tk.Button(root, text="Добавить книгу", command=add_book)

add_label.pack()
title_label.pack()
title_entry.pack()
author_label.pack()
author_entry.pack()
add_button.pack()

# Создаем интерфейс для бронирования и удаления книг
reserve_label = tk.Label(root, text="Бронировать/Удалить книгу")
book_listbox = tk.Listbox(root)
reserve_button = tk.Button(root, text="Бронировать книгу", command=reserve_book)
delete_button = tk.Button(root, text="Удалить книгу", command=delete_book)

reserve_label.pack()
book_listbox.pack()
reserve_button.pack()
delete_button.pack()

# Запускаем главный цикл приложения
root.mainloop()
