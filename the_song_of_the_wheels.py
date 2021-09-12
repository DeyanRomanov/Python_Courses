number = int(input())

counter = 0
my_password = ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == number and a < b and c > d:
                    counter += 1
                    if counter == 4:
                        my_password = f'{a}{b}{c}{d}'
                    print(f'{a}{b}{c}{d}', end=' ')
if counter >= 4:
    print(f'\nPassword: {my_password}')
else:
    print('\nNo!')
