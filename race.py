class Race:
    __RAISE_MESSAGE = "Name cannot be an empty string!"

    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError(self.__RAISE_MESSAGE)
        self.__name = value
