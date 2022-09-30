import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('TK Calculator!')
        self.resizable(0, 0)
        self.configure(background="white")
        for i in range(4):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
        for m in get_monitors():
            if m.is_primary:
                self.create_view(int(m.width/120), int(m.height/180), int(m.width/320))
                #print(m.height/180, m.width/320)

    def create_view(self, font, button_height, button_width):
        style = ttk.Style()
        style.theme_use('clam')
        style.map('TButton', background=[('!active', '#b0b0b0'), ('active', '#d4d4d4')],
                  foreground=[('!active', 'white'), ('active', 'white')])
        style.configure('TButton', font=('Verdana', font), borderwidth=0, height=button_height, width=button_width)
        style.map('special.TButton', background=[('!active', '#ff9466'), ('active', '#ffbda1')],
                  foreground=[('!active', 'white'), ('active', 'white')])
        style.map('op.TButton', background=[('!active', '#7588ff'), ('active', '#9ca9ff')],
                  foreground=[('!active', 'white'), ('active', 'white')])
        style.configure("TLabel", font=('Verdana', font), foreground="#383838")

        label = ttk.Label(self, text='')
        label.grid(column=0, row=0, columnspan=3, sticky=tk.N, padx=3, pady=3)
        label.configure(background="white")
        erase = ttk.Button(self, text="⬅", style='special.TButton', command=lambda: self.erase(label))
        erase.grid(column=3, row=0, sticky=tk.N, padx=3, pady=3)
        buttons = ['789/', '456x', '123-']
        for i in range(3):
            for j in range(4):
                if j < 3:
                    ttk.Button(self, text=buttons[i][j],
                               command=lambda text=buttons[i][j]: self.change_text(label, text))\
                        .grid(column=j, row=i + 1, padx=3, pady=3)
                else:
                    ttk.Button(self, text=buttons[i][j], style='op.TButton',
                               command=lambda text=buttons[i][j]: self.change_text(label, text))\
                        .grid(column=j, row=i + 1, padx=3, pady=3)
        zero = ttk.Button(self, text="0", command=lambda text="0": self.change_text(label, text))
        zero.grid(column=0, row=4, padx=3, pady=3)
        equals = ttk.Button(self, text="=", style='special.TButton', command=lambda: self.calculate(label))
        equals.grid(column=1, columnspan=2, row=4, padx=3, pady=3, ipadx=button_width*8)
        sum = ttk.Button(self, text="+", style='op.TButton', command=lambda text="+": self.change_text(label, text))
        sum.grid(column=3, row=4, padx=3, pady=3)

    def change_text(self, label, text):
        if str(type(label['text'])) != "<class 'str'>":
            label['text'] = text
        else:
            label['text'] += text

    def erase(self, label):
        if str(type(label['text'])) != "<class 'str'>":
            label['text'] = ''
        else:
            label['text'] = label['text'][0:-1]

    def calculate(self, label):
        print(label['text'])


if __name__ == "__main__":
    app = App()
    app.mainloop()
