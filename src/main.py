import sys
"""Для получения абсолютного пути"""
import os
from tkinter import *
"""Для создания графического интерфейса"""



"""Глобальная переменная нужна чтобы код не выдавал ошибки"""
text_area = None



def ls_command(*args):
    """
    Функция, вызванная командой заглушкой
    :param args: любой массив
    :return: нет
    """
    text_area.insert(END, f"ls {' '.join(args)}")
    """
    arg_list = {
        "example": "example"
    }
    if args[0] in arg_list:
        text_area.insert(END, f"ls {' '.join(args)}")
    else:
        text_area.insert(END, "Введены неверные аргументы")
    """

def cd_command(*args):
    """
    Функция, вызванная командой заглушкой
    :param args: любой массив
    :return: нет
    """
    text_area.insert(END, f"cd {' '.join(args)}")
    """
    arg_list = {
        "example": "example"
    }
    if args[0] in arg_list:
        text_area.insert(END, f"ls {' '.join(args)}")
    else:
        text_area.insert(END, "Введены неверные аргументы")
    """

def exit_command(*args):
    """
    Функция, вызванная коммандой выхода из программы
    Выходит из программы
    :param args: Вообще сюда должно быть передано пустое множество
    :return: нет
    """
    sys.exit(0)



def process_command(event):
    """
    Функция по выполнению комманд
    :param event:
    :return: break
    """

    commands = {
        "ls": ls_command,
        "cd": cd_command,
        "exit": exit_command
    }

    current_line = text_area.get("insert linestart", "insert lineend")

    command, *args = current_line.split(" ")

    text_area.insert(END, "\n")

    if command in commands:
        commands[command](*args)
    else:
        text_area.insert(END, "Введена неправильная команда")

    text_area.insert(END, "\n")

    text_area.see(END)

    return "break"



def check_protection(event):
    """
    Защита: разрешает писать только на самой последней строке
    :param event:
    :return: break
    """

    """Получаем индекс первой строки"""
    last_line_start = text_area.index("end-1c linestart")

    """Если курсор находится выше этой строки — блокируем любой ввод или стирание"""
    if text_area.compare("insert", "<", last_line_start):
        return "break"

    """Защита от Backspace: не даем пользователю стереть перенос строки и уйти на строку выше"""
    if event.keysym == "BackSpace" and text_area.compare("insert", "==", last_line_start):
        return "break"



def execute_main():
    """
    Главная функция программы
    :return: а вот ничего она не возвращает беееее
    """

    global text_area

    window = Tk()

    """Настройка GUI"""
    script_path = os.path.abspath(__file__)
    window.title(str(script_path))
    """Ето нада, чтобы указать VFS в заголовке окна"""

    window.geometry("600x600")
    window.resizable(width=False, height=False)

    window.iconbitmap('../icon.ico')


    """Текстовое окно"""
    text_area = Text(window, bg="#1e1e1e", fg="#f1f1f1", font=("Courier", 12), insertbackground="white")
    text_area.pack(fill=BOTH, expand=True)

    """Вот это надо чтобы прошлый текст можно было только читать"""
    text_area.bind("<Key>", check_protection)

    """Привязываем клавишу Enter"""
    text_area.bind("<Return>", process_command)

    text_area.focus_set()

    window.mainloop()



if __name__ == '__main__':
    try:
        execute_main()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
        sys.exit(0)