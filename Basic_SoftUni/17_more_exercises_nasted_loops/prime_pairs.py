star_number_first = int(input())
start_number_second = int(input())
end_number_first = int(input())
end_number_second = int(input())

is_prime = 0
is_prime_2 = 0
flag = False
flag_2 = False

for x in range(star_number_first, (end_number_first + star_number_first + 1)):
    for y in range(start_number_second, (start_number_second + end_number_second + 1)):
        for prime in range(1, x + 1):
            if x % prime == 0:
                is_prime += 1
                if is_prime < 3:
                    flag = True
                else:
                    flag = False
                    break
        is_prime = 0
        for prime_2 in range(1, y + 1):
            if y % prime_2 == 0:
                is_prime_2 += 1
                if is_prime_2 < 3:
                    flag_2 = True
                else:
                    flag_2 = False
                    break
        is_prime_2 = 0
        if flag and flag_2:
            print(f'{x}{y}')
