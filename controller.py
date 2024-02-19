"""Controller module for the calculator."""

from model import Model


class Controller:
    """Controller class for handling calculator operations."""

    def __init__(self):
        """Initialize the Controller."""
        self.model = Model()

    def calculator(self, expression):
        """Evaluate the expression and save it to the model."""
        try:
            current_text = expression
            result = eval(current_text)  # pylint: disable=eval-used
            self.model.save(expression, result)
            return result
        except Exception as exception:  # pylint: disable=broad-except
            return exception
