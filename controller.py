import math
from model import Model


class Controller:
    def __init__(self):
        self.model = Model()

    def calculator(self, expression):
        try:
            current_text = expression
            result = eval(current_text)
            self.model.save(expression, result)
            return result
        except Exception as e:
            return e
