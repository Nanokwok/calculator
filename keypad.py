"""make keypad"""
import tkinter as tk
from tkinter import ttk


class Keypad(tk.Frame):
    """Keypad widget for a calculator."""

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        """Initialize the keypad."""
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad with buttons."""
        for i in range(columns):
            self.grid_columnconfigure(i, weight=1)
        for j in range(len(self.keynames) // columns + 1):
            self.grid_rowconfigure(j, weight=1)

        for i, key in enumerate(self.keynames):
            button = ttk.Button(self, text=key)
            button.grid(row=i // columns, column=i % columns, sticky='nsew')

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to all buttons."""
        for button in self.winfo_children():
            button.bind(sequence, func, add)

    @property
    def frame(self):
        """Return a reference to the frame containing the buttons."""
        return self

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons."""
        for button in self.winfo_children():
            button.configure(cnf, **kwargs)


if __name__ == '__main__':
    keys = list('789456123 0.')

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
