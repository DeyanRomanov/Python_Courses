number_of_chars = int(input())

sum_of_chars = 0

for chars in range(number_of_chars):
    character = input()
    sum_of_chars += ord(character)

print(f'The sum equals: {sum_of_chars}')
