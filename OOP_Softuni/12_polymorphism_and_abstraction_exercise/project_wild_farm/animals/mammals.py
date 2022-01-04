from project_wild_farm.animals.animal import Mammals


class Mouse(Mammals):
    FOOD_TYPE = ['Fruit', 'Vegetable']
    WEIGHT_MULTIPLIER = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammals):
    FOOD_TYPE = ['Meat']
    WEIGHT_MULTIPLIER = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammals):
    FOOD_TYPE = ['Vegetable', 'Meat']
    WEIGHT_MULTIPLIER = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammals):
    FOOD_TYPE = ['Meat']
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
