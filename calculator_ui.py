"""ui for calculator"""
import tkinter as tk
from tkinter import ttk
from keypad import Keypad
from controller import Controller
from model import Model


class CalculatorUI(tk.Tk):
    """CalculatorUI class represents the main calculator user interface."""

    def __init__(self, controller: Controller):
        """Initialize the CalculatorUI."""
        super().__init__()
        self.equation = ''
        self.math_combo = None
        self.display_label = None
        self.title("Calculator")
        self.controller = controller
        self.display_text = tk.StringVar()
        self.history_text = tk.StringVar()
        self.model = Model()
        self.display_text.set("")
        self.init_display()
        self.init_math_combo()
        self.init_keypads()
        self.history_eq_combo()
        self.history_ans_combo()

    def init_display(self):
        """Initialize the display labels."""
        self.display_label = ttk.Label(self, textvariable=self.display_text,
                                       font=('Arial', 20), justify='right', anchor='e')
        self.display_label.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

        self.history_show = ttk.Label(self, textvariable=self.history_text,
                                      font=('Arial', 20), justify='right', anchor='e')
        self.history_show.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        for i in range(1, 2):
            self.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)

    def init_math_combo(self):
        """Initialize the math function combobox."""
        self.math_combo = ttk.Combobox(self, values=['exp', 'ln', 'log10', 'log2', 'sqrt'])
        self.math_combo.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
        self.math_combo.bind("<<ComboboxSelected>>", self.handle_combobox_event)

    def init_keypads(self):
        """Initialize the keypads."""
        keypad_num = Keypad(self, keynames=['7', '8', '9', '4', '5', '6',
                                            '1', '2', '3', '', '0', '.'], columns=3)
        keypad_num.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)
        keypad_num.bind('<Button-1>', self.handle_keypad_event)

        keypad_operator = Keypad(self, keynames=['+', '-', '*', '^', '/', '=',
                                                 '(', ')', 'DEL', 'CLR'], columns=1)
        keypad_operator.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)
        keypad_operator.bind('<Button-1>', self.handle_keypad_event)

    def handle_combobox_event(self):
        """Handle combobox event."""
        function = self.math_combo.get()
        current_text = self.display_text.get()

        if function in ['exp', 'ln', 'log10', 'log2', 'sqrt'] \
                and (not current_text or current_text[-1] in ['+', '-', '*', '^', '/']):
            self.display_text.set(current_text + function + '(')
        elif function in ['exp', 'ln', 'log10', 'log2', 'sqrt']:
            self.display_text.set(function + '(' + current_text + ')')

    def history_eq_combo(self):
        """Initialize the equation history combobox."""
        self.history_combo_lst = []
        self.history_combo = ttk.Combobox(self, values=self.history_combo_lst, state='readonly')
        self.history_combo.grid(row=6, column=0, columnspan=1, sticky='news')
        self.history_combo.bind("<<ComboboxSelected>>", self.handle_history)

    def history_ans_combo(self):
        """Initialize the answer history combobox."""
        self.history_ans_lst = []
        self.history_ans = ttk.Combobox(self, values=self.history_ans_lst, state='readonly')
        self.history_ans.grid(row=6, column=1, columnspan=1, sticky='news')
        self.history_ans.bind("<<ComboboxSelected>>", self.handle_history)

    def handle_replace(self, text):
        """Replace math functions in the text with corresponding Python functions."""
        replace = ['exp', 'ln', 'log10', 'log2', 'sqrt', '^']
        self.equation = text
        for i in replace:
            if i in text:
                if i == '^':
                    self.equation = text.replace(i, '**')
                elif i == 'ln':
                    self.equation = text.replace(i, 'math.log')
                elif i == 'log10':
                    self.equation = text.replace(i, 'math.log10')
                elif i == 'log2':
                    self.equation = text.replace(i, 'math.log2')
                else:
                    self.equation = text.replace(i, 'math.' + i)

    def handle_keypad_event(self, event):
        """Handle keypad events."""
        button_text = event.widget['text']
        current_text = self.display_text.get()
        if button_text == '=':
            self.handle_replace(current_text)
            result = self.controller.calculator(self.equation)
            style = ttk.Style()
            if isinstance(result, Exception):
                style.configure('Custom.TLabel', foreground='red')
                self.bell()
            else:
                self.model.save(current_text, result)
                history = self.model.history[-1]
                self.history_combo_lst.append(history[0])
                self.history_ans_lst.append(history[1])

                self.history_combo['value'] = self.history_combo_lst
                self.history_ans['value'] = self.history_ans_lst

                self.history_combo.current(len(self.history_combo_lst) - 1)
                self.history_ans.current(len(self.history_ans_lst) - 1)

                self.history_text.set(f"{history[0]} = {history[1]}")
                style.configure('Custom.TLabel', foreground='white')
                self.display_text.set(str(result))
            self.display_label.config(style='Custom.TLabel')
        elif button_text == 'CLR':
            self.display_text.set("")
        elif button_text == 'DEL':
            self.display_text.set(current_text[:-1])
        else:
            self.display_text.set(current_text + button_text)

    def handle_history(self, event):
        """Handle history selection."""
        self.display_text.set(event.widget.get())

    def run(self):
        """Run the calculator application."""
        self.mainloop()
