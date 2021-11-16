from collections import deque


def numbers_searching(*args):
    numbers = deque(sorted(args))
    start_range = min(numbers)
    end_range = max(numbers)
    missing_number = ''
    duplicate_numbers = []
    for x in range(start_range, end_range + 1):
        if x not in numbers:
            missing_number = x

    while numbers:
        number = numbers.popleft()
        if number in numbers:
            duplicate_numbers.append(number)
    return [missing_number, duplicate_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))