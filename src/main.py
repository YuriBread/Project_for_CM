import sys
import os
from email.mime import text
from multiprocessing.dummy import current_process

from utils.commands_defs import *
"""Для получения абсолютного пути"""

from tkinter import *
"""Для создания графического интерфейса"""


"""КОД ГОВНА - РАБОТАЕТ, НО ХУЁВО, ПЕРЕДЕЛАТЬ"""


def process_command(event):
    """
    Функция по выполнению комманд
    :param event: на вход строка введенная в окошко
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

    """Вот тут выполнение команды въебать нада желательно"""

    text_area.insert(END)

    """Вот тут говорим что выше больше писать низя"""
    text_area.tag_remove("readonly", "1.0", END)
    text_area.tag_add("readonly", "1.0", "insert linestart")

    text_area.see(END)

    return "break"


def execute_main():
    """
    Главная функция программы
    :return: а вот ничего она не возвращает беееее
    """

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
    text_area.tag_config("readonly", background="#1e1e1e")
    text_area.bind("<Key>", lambda e: "break" if "readonly" in text_area.tag_names("insert") else None)

    """Привязываем клавишу Enter"""
    text_area.bind("<Return>", process_command)

    window.mainloop()

    """
        if command in commands:
            
                                                           Сделать тут проверку аргументов
            commands[command](*args)
        else:
            print("Ошибка! Неизвестная комманда")"""

if __name__ == '__main__':
    try:
        execute_main()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
        sys.exit(0)