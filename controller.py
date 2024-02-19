"""Controller module for the calculator application."""
import math
from model import Model


class Controller:
    """Controller for the calculator application."""
    def __init__(self):
        self.model = Model()

    def calculator(self, expression):
        """Evaluate the expression and save the result."""
        try:
            result = eval(expression)
            return result
        except Exception as error:
            return error
