class Model:
    def __init__(self):
        self.history = []

    def save(self, expression, result):
        self.history.append((expression, result))


