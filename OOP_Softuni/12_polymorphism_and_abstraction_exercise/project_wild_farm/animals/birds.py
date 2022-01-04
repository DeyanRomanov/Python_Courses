from project_wild_farm.animals.animal import Bird


class Owl(Bird):
    FOOD_TYPE = ['Meat']
    WEIGHT_MULTIPLIER = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return f"Hoot Hoot"


class Hen(Bird):
    FOOD_TYPE = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    WEIGHT_MULTIPLIER = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"
