import tkinter as tk

from FileManager import FileManager


def main():
    root = tk.Tk()
    app = FileManager(root)

    # Добавляем меню
    menubar = tk.Menu(root)

    # Меню Файл
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Новая папка", command=app.create_new_folder)
    file_menu.add_separator()
    file_menu.add_command(label="Вставить", command=app.paste_files)
    file_menu.add_separator()
    file_menu.add_command(label="Выход", command=root.quit)
    menubar.add_cascade(label="Файл", menu=file_menu)

    root.config(menu=menubar)
    root.mainloop()


if __name__ == "__main__":
    main()