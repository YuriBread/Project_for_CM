"""
Библиотека самописных функций выполняющих комманды в консоли
"""
import sys

def ls_command(*args):
    print(f"ls {" ".join(args)}")

def cd_command(*args):
    print(f"cd {" ".join(args)}")

def exit_command(*args):
    sys.exit(0)