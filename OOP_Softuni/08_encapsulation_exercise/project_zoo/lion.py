from project_zoo.animal import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name, age, gender):
        super().__init__(name, gender, age, Lion.MONEY_FOR_CARE)

