def factoriel(num_1, num_2):
    for num in range(num_1 - 1, num_2, -1):
        num_1 *= num
    return f'{num_1:.2f}'


number_one = int(input())
number_two = int(input())

print(factoriel(number_one, number_two))
