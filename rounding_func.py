def round_numbers(numbers):
    return list(map(round, numbers))


random_float_number = [float(n) for n in input().split()]
print(round_numbers(random_float_number))
