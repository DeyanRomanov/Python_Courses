import math


def longer(x, y, z, d):
    long = abs(x)**2 + abs(y)**2
    l_1 = abs(z)**2 + abs(d)**2
    if long > l_1:
        return print(f'({math.floor(x)}, {math.floor(y)})')
    else:
        return print(f'({math.floor(z)}, {math.floor(d)})')


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

longer(x_1, y_1, x_2, y_2)
