import tkinter as tk
from tkinter import ttk


# TODO Keypad should extend Frame so that it is a container
class Keypad(ttk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        # TODO call the superclass constructor with all args except
        # keynames and columns
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        key = self.keynames
        for i in range(columns):
            self.grid_columnconfigure(i, weight=1)
        for j in range(len(key) // columns + 1):
            self.grid_rowconfigure(j, weight=1)

        for i in key:
            button = ttk.Button(self, text=i)
            button.grid(row=(key.index(i) // columns), column=(key.index(i) % columns), sticky='nsew')


            # button.bind('<Button-1>', sticky='nsew')
        #     self.grid_rowconfigure(key.index(i) // columns, weight=1, uniform='row')
        #     self.grid_columnconfigure(key.index(i) % columns, weight=1, uniform='column')
        # #
        # for i in range(len(key) // columns + 1):
        #     self.grid_rowconfigure(i, weight=1)
        #     self.grid_columnconfigure(i, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        # TODO Write a bind method with exactly the same parameters
        # as the bind method of Tkinter widgets.
        # Use the parameters to bind all the buttons in the keypad
        # to the same event handler.
        for button in self.winfo_children():
            button.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.winfo_children():
            button[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        for button in self.winfo_children():
            return button[key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """

        # TODO Write a property named 'frame' the returns a reference to
        # the the superclass object for this keypad.
        # This is so that a programmer can set properties of a keypad's frame,
        # e.g. keypad.frame.configure(background='blue')
        for button in self.winfo_children():
            button.configure(cnf, **kwargs)


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
