import tkinter as tk
from tkinter import ttk
from keypad import Keypad


class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.math_combo = None
        self.display_label = None
        self.title("Calculator")
        self.display_text = tk.StringVar()
        self.display_text.set("")
        self.init_display()
        self.init_math_combo()
        self.init_keypads()

    def init_display(self):
        self.display_label = ttk.Label(self, textvariable=self.display_text, font=('Arial', 20), justify='right',
                                       anchor='e')
        self.display_label.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def init_math_combo(self):
        self.math_combo = ttk.Combobox(self, values=['exp', 'ln', 'log10', 'log2', 'sqrt'])
        self.math_combo.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
        self.math_combo.bind("<<ComboboxSelected>>", self.handle_combobox_event)

    def init_keypads(self):
        keypad_num = Keypad(self, keynames=['7', '8', '9', '4', '5', '6', '1', '2', '3', '', '0', '.'], columns=3)
        keypad_num.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
        keypad_num.bind('<Button-1>', self.handle_keypad_event)

        keypad_operator = Keypad(self, keynames=['+', '-', '*', '^', '/', '=', 'DEL', 'CLR'], columns=1)
        keypad_operator.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
        keypad_operator.bind('<Button-1>', self.handle_keypad_event)

    def handle_combobox_event(self, event):
        function = self.math_combo.get()
        if function in ['exp', 'ln', 'log10', 'log2', 'sqrt']:
            self.display_text.set(self.display_text.get() + function + '(')

    def handle_keypad_event(self, event):
        button_text = event.widget['text']
        current_text = self.display_text.get()
        if button_text == '=':
            try:
                result = eval(current_text.replace("^", "**"))
                self.display_text.set(str(result))
            except Exception as e:
                self.display_text.set("Error")
        elif button_text == 'CLR':
            self.display_text.set("")
        elif button_text == 'DEL':
            self.display_text.set(current_text[:-1])
        else:
            self.display_text.set(current_text + button_text)

    def run(self):
        self.mainloop()
