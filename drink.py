from project_zoo.product import Product


class Drink(Product):

    def __init__(self, name):
        super().__init__(name, 10)
