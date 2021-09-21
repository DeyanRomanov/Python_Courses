start_number = int(input())
end_number = int(input())
for number_one in range(start_number, end_number + 1):
    for number_two in range(start_number, end_number + 1):
        for number_three in range(start_number, end_number + 1):
            for number_four in range(start_number, end_number + 1):
                if number_one > number_four and (number_three + number_two) % 2 == 0:
                    if number_one % 2 == 0 and number_four % 2 != 0:
                        print(f'{number_one}{number_two}{number_three}{number_four}', end=' ')
                    elif number_four % 2 == 0 and number_one % 2 != 0:
                        print(f'{number_one}{number_two}{number_three}{number_four}', end=' ')
                    else:
                        continue
                else:
                    continue
