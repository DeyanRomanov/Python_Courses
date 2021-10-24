number_of_numbers = int(input())

stack = []

for _ in range(number_of_numbers):
    number = [int(el) for el in input().split()]
    if number[0] == 1:
        stack.append(number[1])
    elif number[0] == 2:
        if stack:
            stack.pop()
    elif number[0] == 3:
        if stack:
            print(max(stack))
    elif number[0] == 4:
        if stack:
            print(min(stack))

reversed_stack = []
for _ in range(len(stack)):
    reversed_stack.append(str(stack.pop()))
print(', '.join(reversed_stack))
