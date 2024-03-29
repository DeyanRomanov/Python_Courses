class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.diameter * self.__pi

    def calculate_area(self):
        r = self.diameter / 2
        return self.__pi * r**2

    def calculate_area_of_sector(self, angle):
        r = self.diameter / 2
        return (angle / 360) * (self.__pi * r**2)


diamet = float(input())
angle = float(input())
circle = Circle(diamet)

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")


