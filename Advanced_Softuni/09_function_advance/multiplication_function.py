from functools import reduce


def multiply(*args):
    result = reduce(lambda x, y: x * y, args)
    return result


random_float_number = [int(n) for n in input().split(', ')]
print(multiply(*random_float_number))
