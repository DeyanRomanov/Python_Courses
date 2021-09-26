number = int(input())

prime_counter = 0
for x in range(1, number + 1):
    if number % x == 0:
        prime_counter += 1
if prime_counter > 2:
    print(f'False')
else:
    print(f'True')
