numbers = input().split('|')

result, reversed_result = [], []

for res in [numbers[i].split() for i in range(len(numbers) - 1, -1, -1)]:
    reversed_result.extend(res)

print(' '.join(reversed_result))
