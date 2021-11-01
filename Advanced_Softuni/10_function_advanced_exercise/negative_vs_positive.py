def negative_positive(numbers):
    negative_numbers = sum(filter(lambda x: x < 0, numbers))
    positives_numbers = sum(filter(lambda x: x > 0, numbers))
    if abs(negative_numbers) > positives_numbers:
        return print(f'{negative_numbers}\n{positives_numbers}\nThe negatives are stronger than the positives')
    return print(f'{negative_numbers}\n{positives_numbers}\nThe positives are stronger than the negatives')


random_numbers = [int(x) for x in input().split()]

negative_positive(random_numbers)
