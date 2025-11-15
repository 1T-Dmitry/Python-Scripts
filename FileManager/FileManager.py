import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import shutil
from pathlib import Path
from datetime import datetime

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Файловый менеджер")
        self.root.geometry("1000x800")
        self.root.iconbitmap(default="favicon.ico")

        self.current_path = Path.home()

        self.create_widgets()
        self.load_directory()

    def create_widgets(self):
        # Верхняя панель с навигацией
        self.create_navigation_bar()

        # Основная область с файлами
        self.create_file_list()

        # Нижняя панель статуса
        self.create_status_bar()

        # Контекстное меню
        self.create_context_menu()

    def create_navigation_bar(self):
        # Фрейм для навигации
        nav_frame = ttk.Frame(self.root)
        nav_frame.pack(fill=tk.X, padx=5, pady=5)

        # Кнопка "Наверх"
        ttk.Button(nav_frame, text="↑", width=3,
                   command=self.go_up).pack(side=tk.LEFT)

        # Поле текущего пути
        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(nav_frame, textvariable=self.path_var, width=70)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.path_entry.bind("<Return>", self.on_path_enter)

        # Кнопка обновления
        ttk.Button(nav_frame, text="Обновить",
                   command=self.load_directory).pack(side=tk.LEFT, padx=2)

        # Поле поиска
        ttk.Label(nav_frame, text="Поиск:").pack(side=tk.LEFT, padx=(10, 2))
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(nav_frame, textvariable=self.search_var, width=20)
        self.search_entry.pack(side=tk.LEFT, padx=2)
        self.search_entry.bind("<KeyRelease>", self.on_search)

    def create_file_list(self):
        # Фрейм для списка файлов
        list_frame = ttk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Создаем Treeview для отображения файлов
        columns = ("name", "size", "type", "modified")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")

        # Настраиваем колонки
        self.tree.heading("name", text="Имя")
        self.tree.heading("size", text="Размер")
        self.tree.heading("type", text="Тип")
        self.tree.heading("modified", text="Изменен")

        self.tree.column("name", width=300)
        self.tree.column("size", width=100)
        self.tree.column("type", width=100)
        self.tree.column("modified", width=150)

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Бинды событий
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<Button-3>", self.show_context_menu)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Готов")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_context_menu(self):
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Открыть", command=self.open_selected)
        self.context_menu.add_command(label="Копировать", command=self.copy_selected)
        self.context_menu.add_command(label="Переместить", command=self.move_selected)
        self.context_menu.add_command(label="Удалить", command=self.delete_selected)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Переименовать", command=self.rename_selected)
        self.context_menu.add_command(label="Свойства", command=self.show_properties)

    def create_new_folder(self):
        """Создает новую папку в текущей директории"""
        new_name = tk.simpledialog.askstring("Новая папка", "Введите имя новой папки:")
        if new_name:
            try:
                new_path = self.current_path / new_name
                new_path.mkdir(exist_ok=False)
                self.load_directory()
                self.status_var.set(f"Создана папка: {new_name}")
            except FileExistsError:
                messagebox.showerror("Ошибка", f"Папка '{new_name}' уже существует")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось создать папку: {e}")

    def show_properties(self):
        """Показывает свойства выбранного файла/папки"""
        paths = self.get_selected_paths()
        if len(paths) == 1:
            path = paths[0]
            try:
                stat = path.stat()

                # Собираем информацию о файле/папке
                if path.is_dir():
                    file_type = "Папка"
                    size = self.get_folder_size_details(path)
                else:
                    file_type = self.get_file_type(path)
                    size = self.get_file_size(path)

                # Форматируем время
                created = datetime.fromtimestamp(stat.st_ctime).strftime("%d.%m.%Y %H:%M:%S")
                modified = datetime.fromtimestamp(stat.st_mtime).strftime("%d.%m.%Y %H:%M:%S")
                accessed = datetime.fromtimestamp(stat.st_atime).strftime("%d.%m.%Y %H:%M:%S")

                # Создаем окно с информацией
                properties_window = tk.Toplevel(self.root)
                properties_window.title(f"Свойства: {path.name}")
                properties_window.geometry("400x300")
                properties_window.resizable(False, False)

                # Основной фрейм
                main_frame = ttk.Frame(properties_window, padding="10")
                main_frame.pack(fill=tk.BOTH, expand=True)

                # Информация
                info_text = f"""Имя: {path.name}
    Тип: {file_type}
    Размер: {size}
    Расположение: {path.parent}

    Создан: {created}
    Изменен: {modified}
    Последний доступ: {accessed}

    Атрибуты:
    - Только для чтения: {not os.access(path, os.W_OK)}
    - Скрытый: {path.name.startswith('.')}"""

                text_widget = tk.Text(main_frame, wrap=tk.WORD, height=15, width=50)
                text_widget.insert(tk.END, info_text)
                text_widget.config(state=tk.DISABLED)
                text_widget.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

                # Кнопка закрытия
                ttk.Button(main_frame, text="Закрыть",
                           command=properties_window.destroy).pack()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось получить свойства: {e}")
        else:
            messagebox.showinfo("Информация", "Выберите один файл или папку")

    def load_directory(self):
        """Загружает содержимое текущей директории"""
        self.path_var.set(str(self.current_path))

        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            if self.current_path.parent != self.current_path:
                self.tree.insert("", "end", values=("..", "", "Папка", ""), tags=("folder",))

            items = list(self.current_path.iterdir())
            folders = [item for item in items if item.is_dir()]
            files = [item for item in items if item.is_file()]

            for folder in sorted(folders):
                size = self.get_folder_size(folder)
                modified = self.get_modified_time(folder)
                self.tree.insert("", "end", values=(
                    folder.name, size, "Папка", modified
                ), tags=("folder",))

            for file in sorted(files):
                size = self.get_file_size(file)
                file_type = self.get_file_type(file)
                modified = self.get_modified_time(file)
                self.tree.insert("", "end", values=(
                    file.name, size, file_type, modified
                ), tags=("file",))

            self.tree.tag_configure("folder", foreground="blue")
            self.tree.tag_configure("file", foreground="black")

            self.status_var.set(f"Папка загружена: {len(folders)} папок, {len(files)} файлов")

        except PermissionError:
            messagebox.showerror("Ошибка", "Нет доступа к этой папке")

    def get_file_size(self, file_path):
        """Возвращает размер файла в читаемом формате"""
        try:
            size = file_path.stat().st_size
            if size == 0:
                return "0 B"
            for unit in ['B', 'KB', 'MB', 'GB']:
                if size < 1024.0:
                    return f"{size:.1f} {unit}"
                size /= 1024.0
            return f"{size:.1f} TB"
        except:
            return "?"

    def get_folder_size(self, folder_path):
        """Возвращает примерный размер папки"""
        try:
            return "Папка"
        except:
            return "?"

    def get_file_type(self, file_path):
        """Определяет тип файла по расширению"""
        ext = file_path.suffix.lower()
        type_map = {
            '.txt': 'Текст',
            '.pdf': 'PDF',
            '.jpg': 'Изображение', '.jpeg': 'Изображение', '.png': 'Изображение',
            '.mp3': 'Аудио', '.wav': 'Аудио',
            '.mp4': 'Видео', '.avi': 'Видео',
            '.zip': 'Архив', '.rar': 'Архив', '.7z': 'Архив',
            '.exe': 'Приложение',
            '.py': 'Python скрипт',
        }
        return type_map.get(ext, 'Файл')

    def get_modified_time(self, path):
        """Возвращает время изменения"""
        try:
            from datetime import datetime
            mtime = path.stat().st_mtime
            return datetime.fromtimestamp(mtime).strftime("%d.%m.%Y %H:%M")
        except:
            return "?"

    def on_double_click(self, event):
        """Обработчик двойного клика"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            name = item['values'][0]

            if name == "..":
                self.go_up()
            elif item['tags'] and 'folder' in item['tags']:
                new_path = self.current_path / name
                self.current_path = new_path
                self.load_directory()
            else:
                self.open_selected()

    def go_up(self):
        """Переход на уровень вверх"""
        if self.current_path.parent != self.current_path:
            self.current_path = self.current_path.parent
            self.load_directory()

    def on_path_enter(self, event):
        """Обработчик ввода пути вручную"""
        new_path = Path(self.path_var.get())
        if new_path.exists() and new_path.is_dir():
            self.current_path = new_path
            self.load_directory()
        else:
            messagebox.showerror("Ошибка", "Путь не существует или не является папкой")

    def on_search(self, event):
        """Поиск файлов"""
        search_text = self.search_var.get().lower()
        if not search_text:
            self.load_directory()
            return

        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            for item in self.current_path.iterdir():
                if search_text in item.name.lower():
                    if item.is_dir():
                        self.tree.insert("", "end", values=(
                            item.name, "Папка", "Папка", ""
                        ), tags=("folder",))
                    else:
                        size = self.get_file_size(item)
                        file_type = self.get_file_type(item)
                        modified = self.get_modified_time(item)
                        self.tree.insert("", "end", values=(
                            item.name, size, file_type, modified
                        ), tags=("file",))

            self.tree.tag_configure("folder", foreground="blue")
            self.tree.tag_configure("file", foreground="black")

        except PermissionError:
            messagebox.showerror("Ошибка", "Нет доступа для поиска")

    def get_selected_paths(self):
        """Возвращает список выбранных путей"""
        selections = self.tree.selection()
        paths = []
        for selection in selections:
            item = self.tree.item(selection)
            name = item['values'][0]
            if name != "..":
                paths.append(self.current_path / name)
        return paths

    def open_selected(self):
        """Открывает выбранный файл/папку"""
        paths = self.get_selected_paths()
        if paths:
            path = paths[0]
            if path.is_dir():
                self.current_path = path
                self.load_directory()
            else:
                try:
                    os.startfile(path)  # Windows
                except:
                    try:
                        # Linux/Mac
                        import subprocess
                        subprocess.run(['xdg-open', str(path)])
                    except:
                        messagebox.showerror("Ошибка", "Не удалось открыть файл")

    def copy_selected(self):
        """Копирует выбранные файлы в буфер"""
        self.clipboard_files = self.get_selected_paths()
        self.clipboard_operation = "copy"
        self.status_var.set(f"Выбрано для копирования: {len(self.clipboard_files)} объектов")

    def move_selected(self):
        """Перемещает выбранные файлы в буфер"""
        self.clipboard_files = self.get_selected_paths()
        self.clipboard_operation = "move"
        self.status_var.set(f"Выбрано для перемещения: {len(self.clipboard_files)} объектов")

    def paste_files(self):
        """Вставляет файлы из буфера"""
        if hasattr(self, 'clipboard_files') and self.clipboard_files:
            try:
                for src in self.clipboard_files:
                    dst = self.current_path / src.name
                    if self.clipboard_operation == "copy":
                        if src.is_dir():
                            shutil.copytree(src, dst)
                        else:
                            shutil.copy2(src, dst)
                    else:  # move
                        shutil.move(str(src), str(dst))

                self.load_directory()
                if self.clipboard_operation == "move":
                    self.clipboard_files = []

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось выполнить операцию: {e}")

    def delete_selected(self):
        """Удаляет выбранные файлы"""
        paths = self.get_selected_paths()
        if paths:
            names = "\n".join([p.name for p in paths])
            if messagebox.askyesno("Подтверждение",
                                   f"Удалить выбранные объекты?\n{names}"):
                try:
                    for path in paths:
                        if path.is_dir():
                            shutil.rmtree(path)
                        else:
                            path.unlink()
                    self.load_directory()
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось удалить: {e}")

    def rename_selected(self):
        """Переименовывает выбранный файл"""
        paths = self.get_selected_paths()
        if len(paths) == 1:
            path = paths[0]
            new_name = tk.simpledialog.askstring("Переименование",
                                                 "Введите новое имя:",
                                                 initialvalue=path.name)
            if new_name and new_name != path.name:
                try:
                    new_path = path.parent / new_name
                    path.rename(new_path)
                    self.load_directory()
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось переименовать: {e}")

    def show_context_menu(self, event):
        """Показывает контекстное меню"""
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)

    def on_select(self, event):
        """Обновляет статус при выборе файлов"""
        selected = len(self.tree.selection())
        self.status_var.set(f"Выбрано: {selected} объектов")
