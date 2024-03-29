from abc import ABC, abstractmethod
from project_wild_farm.food import Food


class Animal(ABC):
    FOOD_TYPE = []
    WEIGHT_MULTIPLIER = 1

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        food_name = food.__class__.__name__
        if food_name not in self.FOOD_TYPE:
            return f"{self.__class__.__name__} does not eat {food_name}!"
        self.weight += food.quantity * self.WEIGHT_MULTIPLIER
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammals(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
