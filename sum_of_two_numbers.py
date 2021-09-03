number_one = int(input())
number_two = int(input())
magic_number = int(input())
combination = 0
flag = False
for x in range(number_one, number_two + 1):
    for y in range(number_one, number_two + 1):
        combination += 1
        if x + y == magic_number:
            flag = True
            print(f'Combination N:{combination} ({x} + {y} = {magic_number})')
            break
    if flag:
        break
if not flag:
    print(f"{combination} combinations - neither equals {magic_number}")
