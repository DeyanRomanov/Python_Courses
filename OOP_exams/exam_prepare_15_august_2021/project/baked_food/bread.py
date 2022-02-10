from __exam_prepare_15_august_2021.project.baked_food.baked_food import BakedFood


class Bread(BakedFood):

    def __init__(self, name, price):
        super().__init__(name, 200, price)
