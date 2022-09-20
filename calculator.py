import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

window = tk.Tk()
window.geometry("280x235")
window.title('Bad Calculator!')
window.resizable(0, 0)
window.configure(background="white")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)


def change_text(text):
    if str(type(label['text'])) != "<class 'str'>":
        label['text'] = text
    else:
        label['text'] += text


def calculate():
    number = ''
    numbers = []
    op = ''
    for i in range(len(label['text'])):
        sign = label['text'][i]
        if sign in ['+', '-', '/', 'x']:
            op = sign
            numbers.append(number)
            number = ''
        elif i != len(label['text']) - 1:
            number += sign
        else:
            if op != '':
                number += sign
                numbers.append(number)
                if op and len(numbers) == 2:
                    if op == '+':
                        label['text'] = int(numbers[0]) + int(numbers[1])
                    elif op == '-':
                        label['text'] = int(numbers[0]) - int(numbers[1])
                    elif op == 'x':
                        label['text'] = int(numbers[0]) * int(numbers[1])
                    elif op == '/':
                        try:
                            label['text'] = int(numbers[0]) / int(numbers[1])
                        except ZeroDivisionError:
                            messagebox.showerror("Ошибка", "Деление на ноль!")
                elif len(numbers) > 2:
                    messagebox.showwarning("Внимание", "Работаем только с двумя числами и одной операцией:)")
            else:
                messagebox.showerror("Ошибка", "Нет операций")


def erase():
    if str(type(label['text'])) != "<class 'str'>":
        label['text'] = ''
    else:
        label['text'] = label['text'][0:-1]


label = ttk.Label(window, text='')
label.grid(column=0, row=0, columnspan=3, sticky=tk.N, padx=3, pady=10)
label.configure(background="white")
erase = ttk.Button(window, text="⬅", command=erase, style='my.TButton')
erase.grid(column=3, row=0, sticky=tk.N, padx=3, pady=10)

style = ttk.Style()
style.theme_use('clam')
style.map('TButton', background=[('!active', '#b0b0b0'), ('active', '#d4d4d4')],
          foreground=[('!active', 'white'), ('active', 'white')])
style.configure('TButton', font=('Verdana', 15), borderwidth=0)
style.map('my.TButton', background=[('!active', '#ff9466'), ('active', '#ffbda1')],
          foreground=[('!active', 'white'), ('active', 'white')])
style.map('op.TButton', background=[('!active', '#7588ff'), ('active', '#9ca9ff')],
          foreground=[('!active', 'white'), ('active', 'white')])
style.configure("TLabel", font=('Verdana', 15), foreground="#383838")

seven = ttk.Button(window, text="7", command=lambda text="7": change_text(text))
seven.grid(column=0, row=1, padx=3, pady=3)
eight = ttk.Button(window, text="8", command=lambda text="8": change_text(text))
eight.grid(column=1, row=1, padx=3, pady=3)
nine = ttk.Button(window, text="9", command=lambda text="9": change_text(text))
nine.grid(column=2, row=1, padx=3, pady=3)
divide = ttk.Button(window, text="/", command=lambda text="/": change_text(text), style='op.TButton')
divide.grid(column=3, row=1, padx=3, pady=3)

four = ttk.Button(window, text="4", command=lambda text="4": change_text(text))
four.grid(column=0, row=2, padx=3, pady=3)
five = ttk.Button(window, text="5", command=lambda text="5": change_text(text))
five.grid(column=1, row=2, padx=3, pady=3)
six = ttk.Button(window, text="6", command=lambda text="6": change_text(text))
six.grid(column=2, row=2, padx=3, pady=3)
multiply = ttk.Button(window, text="x", command=lambda text="x": change_text(text), style='op.TButton')
multiply.grid(column=3, row=2, padx=3, pady=3)

one = ttk.Button(window, text="1", command=lambda text="1": change_text(text))
one.grid(column=0, row=3, padx=3, pady=3)
two = ttk.Button(window, text="2", command=lambda text="2": change_text(text))
two.grid(column=1, row=3, padx=3, pady=3)
three = ttk.Button(window, text="3", command=lambda text="3": change_text(text))
three.grid(column=2, row=3, padx=3, pady=3)
subtract = ttk.Button(window, text="-", command=lambda text="-": change_text(text), style='op.TButton')
subtract.grid(column=3, row=3, padx=3, pady=3)

zero = ttk.Button(window, text="0", command=lambda text="0": change_text(text))
zero.grid(column=0, row=4, padx=3, pady=3)
equals = ttk.Button(window, text="=", command=calculate, style='my.TButton')
equals.grid(column=1, columnspan=2, row=4, padx=3, pady=3)
sum = ttk.Button(window, text="+", command=lambda text="+": change_text(text), style='op.TButton')
sum.grid(column=3, row=4, padx=3, pady=3)

window.mainloop()
