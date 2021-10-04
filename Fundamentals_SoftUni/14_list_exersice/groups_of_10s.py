numbers = [int(num) for num in input().split(', ')]

max_number = int(max(numbers))
if not max_number % 2 == 0:
    max_number //= 10
    max_number += 1
else:
    max_number //= 10

while len(numbers) > 0:
    for x in range(1, max_number + 1):
        group_numbers = [num for num in numbers if num <= x * 10]
        print(f"Group of {x * 10}'s: {group_numbers}")
        numbers = [num for num in numbers if num not in group_numbers]
        group_numbers.clear()
