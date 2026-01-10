class Secret:
    def __init__(self, value: str):
        self._value = value

    def get(self):
        return self._value

    def __repr__(self):
        return "<SECRET>"

    def __str__(self):
        return "<SECRET>"
