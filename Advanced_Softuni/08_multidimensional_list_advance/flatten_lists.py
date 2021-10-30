string_with_numbers = input().split('|')

matrix = []
reverse_result = []
for x in range(len(string_with_numbers) - 1, -1, -1):
    reverse_result += string_with_numbers[x].split()

print(' '.join(reverse_result))
