import sys
import os
from cmd import PROMPT
from tkinter import *

text_area = None


def ls_command(*args):
    """
    Функция, вызванная командой заглушкой
    :param args: любой массив
    :return: нет
    """
    arg_list = {"example": "example"}

    if args and args[0] in arg_list:
        text_area.insert(END, f"ls {''.join(args)}")
    elif not args:
        text_area.insert(END, "ls: вывод списка директорий (нет аргументов)")
    else:
        text_area.insert(END, "Введены неверные аргументы")


def cd_command(*args):
    """
    Функция, вызванная командой заглушкой
    :param args: любой массив
    :return: нет
    """
    if args:
        text_area.insert(END, f"cd {''.join(args)}")
    else:
        text_area.insert(END, "cd: не указан путь")

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

    if current_line.startswith(PROMPT):
        current_line = current_line[len(PROMPT):]

    tokens = current_line.strip().split()

    if not tokens:
        text_area.insert(END, f"\n{PROMPT}")
        text_area.see(END)
        return "break"

    command, *args = tokens

    text_area.insert(END, "\n")

    if command in commands:
        commands[command](*args)
    else:
        text_area.insert(END, "Введена неправильная команда")

    text_area.insert(END, f"\n{PROMPT}")

    text_area.see(END)

    return "break"



def check_protection(event):
    """
    Защита: разрешает писать только на самой последней строке
    :param event:
    :return: break
    """

    last_line_start = text_area.index("end-1c linestart")
    prompt_end = text_area.index(f"{last_line_start} + {len(PROMPT)} c")

    allowed_keys = ["Left", "Right", "Up", "Down", "Home", "End", "Control_L", "Control_R"]
    if event.keysym in allowed_keys:
        return None

    if text_area.compare("insert", "<", last_line_start):
        if text_area.compare("insert", "<=", prompt_end):
            return "break"

    if event.keysym == "BackSpace" and text_area.compare("insert", "==", last_line_start):
        return "break"



def execute_main():
    """
    Главная функция программы
    :return: а вот ничего она не возвращает беееее
    """

    global text_area

    window = Tk()

    script_path = os.path.abspath(__file__)
    window.title("VFS main.py   ")

    window.geometry("600x600")
    window.resizable(width=False, height=False)

    window.iconbitmap('../icon.ico')


    text_area = Text(window, bg="#1e1e1e", fg="#f1f1f1", font=("Courier", 12), insertbackground="white")
    text_area.pack(fill=BOTH, expand=True)

    text_area.insert(END, PROMPT)

    text_area.bind("<Key>", check_protection)

    text_area.bind("<Return>", process_command)

    text_area.focus_set()

    window.mainloop()



if __name__ == '__main__':
    try:
        execute_main()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
        sys.exit(0)