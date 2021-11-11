from math import log


def logarithm(numbers, bases):
    if bases == 'natural':
        res = log(numbers)
    else:
        res = log(numbers, int(bases))
    return res


def print_triangle_whit_numbers(numbers):
    for n in range(1, numbers + 1):
        for y in range(1, n + 1):
            print(y, end=' ')
        print()
    for n in range(numbers - 1, 0, -1):
        for y in range(1, n + 1):
            print(y, end=' ')
        print()

