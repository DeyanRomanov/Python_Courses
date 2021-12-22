class Planet:

    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 1:
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self._name = value
