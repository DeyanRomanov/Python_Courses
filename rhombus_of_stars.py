def make_rhombus(value):
    for s in range(1, value + 1):
        print_rhombus(value, s)
    for s in range(value - 1, 0, - 1):
        print_rhombus(value, s)


def print_rhombus(stars_number, x):
    print(f"{' ' * (stars_number - x)}{'* ' * x}")


number_of_stars = int(input())
make_rhombus(number_of_stars)
