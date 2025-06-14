import os
import subprocess
import platform

def open_file(filepath):
    if not os.path.isfile(filepath):
        print("Файл не найден.")
        return
    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(filepath)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", filepath])
        else:  # Linux и др.
            subprocess.run(["xdg-open", filepath])
        print(f"Файл {filepath} открыт в редакторе по умолчанию.")
    except Exception as e:
        print("Ошибка при открытии файла:", e)

def show_file_content(filepath):
    if not os.path.isfile(filepath):
        print("Файл не найден.")
        return
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"\nСодержимое файла '{filepath}':\n")
        print(content)
    except Exception as e:
        print("Ошибка при чтении файла:", e)

def find_files(name_part, search_path="."):
    print(f"Ищем файлы, содержащие '{name_part}' в имени, в папке '{os.path.abspath(search_path)}':")
    found = False
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if name_part.lower() in file.lower():
                print(os.path.join(root, file))
                found = True
    if not found:
        print("Файлы не найдены.")

def list_directory(path):
    if not os.path.isdir(path):
        print("Директория не найдена.")
        return
    print(f"\nСодержимое директории '{os.path.abspath(path)}':")
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print(f"[DIR]  {entry}")
        else:
            print(f"       {entry}")

def main():
    while True:
        print("\nФайловый менеджер:")
        print("1 – Открыть файл")
        print("2 – Показать содержимое файла")
        print("3 – Найти файл/файлы по имени")
        print("4 – Раскрыть директорию")
        print("0 – Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            path = input("Введите путь к файлу: ").strip()
            open_file(path)
        elif choice == "2":
            path = input("Введите путь к файлу: ").strip()
            show_file_content(path)
        elif choice == "3":
            name_part = input("Введите часть или полное имя файла для поиска: ").strip()
            path = input("Введите путь для поиска (по умолчанию текущая директория): ").strip()
            if path == "":
                path = "."
            find_files(name_part, path)
        elif choice == "4":
            path = input("Введите путь к директории: ").strip()
            list_directory(path)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
