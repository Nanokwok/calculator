"""Display the calculator user interface."""
from calculator_ui import CalculatorUI
from controller import Controller


if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    controller = Controller()
    ui = CalculatorUI(controller)
    ui.run()
