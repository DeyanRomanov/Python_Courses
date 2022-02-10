from car.car import Car


class MuscleCar(Car):
    __MIN_SPEED_LIMIT = 250
    __MAX_SPEED_LIMIT = 450
    __RAISE_MESSAGE = f"Invalid speed limit! Must be between {__MIN_SPEED_LIMIT} and {__MAX_SPEED_LIMIT}!"

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.__MIN_SPEED_LIMIT or value > self.__MAX_SPEED_LIMIT:
            raise ValueError(self.__RAISE_MESSAGE)
        self.__speed_limit = value
