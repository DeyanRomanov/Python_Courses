numbers = int(input())

sum_from_nums = 0
for number in range(1, numbers + 1):
    for letter in str(number):
        sum_from_nums += int(letter)
    if sum_from_nums == 5 or sum_from_nums == 7 or sum_from_nums == 11:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')
    sum_from_nums = 0

