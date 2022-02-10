from astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATH_UNIT = 5

    def __init__(self, name):
        super().__init__(name, 70)
