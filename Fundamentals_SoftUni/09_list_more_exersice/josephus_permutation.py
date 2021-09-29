numbers = input().split()
steps = int(input())

step = 0
permutaion = []
permutation_as_string = 0

while len(numbers) > 0:
    step += steps - 1
    if step < len(numbers):
        permutaion.append(numbers[step])
        numbers.pop(step)
    else:
        step -= len(numbers) + steps - 1

permutation_as_string = '['

for y, x in enumerate(permutaion):
    if y == len(permutaion) - 1:
        permutation_as_string += x
    else:
        permutation_as_string += f'{x},'
permutation_as_string += ']'

print(permutation_as_string)