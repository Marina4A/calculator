from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
from operator import add, sub, mul, truediv


class Calculator:

    def __init__(self):
        self.bttn_list = [
            "7", "8", "9", "+", "*",
            "4", "5", "6", "-", "/",
            "1", "2", "3", "=", "xⁿ",
            "0", ".", "±", "C",
            "Exit", "π", "sin", "cos",
            "(", ")", "n!", "√2", ]
        self.build()

    def build(self):
        r = 1
        c = 0
        for i in self.bttn_list:
            rel = ""
            cmd = lambda x=i: calc(x)
            ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
            c += 1
            if c > 4:
                c = 0
                r += 1

    def calc(key):
        global memory
        if key == "=":
            # исключение написания слов
            str1 = "-+0123456789.*/)("
            if calc_entry.get()[0] not in str1:
                calc_entry.insert(END, "First symbol is not number!")
                messagebox.showerror("Error!", "You did not enter the number!")
            # исчисления
            try:
                result = eval(calc_entry.get())
                calc_entry.insert(END, "=" + str(result))
            except:
                calc_entry.insert(END, "Error!")
                messagebox.showerror("Error!", "Check the correctness of data")


if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")


text = 'https://habr.com/ru/sandbox/115348/'