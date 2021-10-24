stack = input().split()

reversed_numbers = []

while stack:
    reversed_numbers.append(stack.pop())

print(' '.join(reversed_numbers))
