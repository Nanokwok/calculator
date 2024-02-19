class Model:
    """Model class for storing calculation history."""

    def __init__(self):
        """Initialize the Model."""
        self.history = []

    def save(self, expression, result):
        """Save the expression and result to the history."""
        self.history.append((expression, result))
