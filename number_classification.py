numbers = [int(num) for num in input().split(', ')]
positive = []
negative = []
[positive.append(num) if num <= 0 else negative.append(num) for num in numbers]
even = []
odd = []
[even.append(num) if num % 2 == 0 else odd.append(num) for num in numbers]

print(f'Positive: {", ".join(str(num) for num in positive)}')
print(f'Negative: {", ".join(str(num) for num in negative)}')
print(f'Even: {", ".join(str(num) for num in even)}')
print(f'Odd: {", ".join(str(num) for num in odd)}')
