number = int(input())
symbol_x = 0
symbol_y = 0
for x in range(1, number + 1):
    if x == 1 or x == number:
        symbol_x = '+'
    else:
        symbol_x = '|'
    print(f'{symbol_x}', end=' ')
    for y in range(1, number - 1, 1):
        symbol_y = '-'
        print(f'{symbol_y}', end=' ')
    print(f'{symbol_x}')

