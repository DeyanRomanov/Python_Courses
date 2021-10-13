import math
letters_and_nums = input().split()

total_sum = 0
for el in letters_and_nums:
    counter = 0
    first_letter = el[0]
    last_letter = el[-1]
    num = int(el[1:-1])
    if first_letter.isupper():
        first_letter = int(ord(first_letter) - 64)
        counter = num / first_letter
    else:
        first_letter = int(ord(first_letter) - 96)
        counter = num * first_letter
    if last_letter.isupper():
        last_letter = int(ord(last_letter) - 64)
        counter -= last_letter
    else:
        last_letter = int(ord(last_letter) - 96)
        counter += last_letter
    total_sum += counter

print(f'{total_sum:.2f}')
