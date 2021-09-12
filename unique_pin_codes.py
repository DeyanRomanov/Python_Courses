first_number_stop = int(input())
second_number_stop = int(input())
tird_number_stop = int(input())

prime_counter = 0

for number_one in range(1, first_number_stop + 1):
    for number_two in range(1, second_number_stop + 1):
        for number_three in range(1, tird_number_stop + 1):
            if number_one % 2 == 0 and number_three % 2 == 0:
                for prime in range(1, number_two + 1):
                    if number_two % prime == 0:
                        prime_counter += 1
                if prime_counter == 2:
                    print(f'{number_one} {number_two} {number_three}')
                prime_counter = 0
