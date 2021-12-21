class Driver:
    __RAISE_MESSAGE = f"Name should contain at least one character!"
    def __init__(self, name):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError(self.__RAISE_MESSAGE)
        self.__name = value
