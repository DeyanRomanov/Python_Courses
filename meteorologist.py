from astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    BREATH_UNIT = 15

    def __init__(self, name):
        super().__init__(name, 90)
