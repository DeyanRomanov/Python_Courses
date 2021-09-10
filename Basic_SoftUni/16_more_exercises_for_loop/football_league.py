stadium_capacity = int(input())
all_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for x in range(all_fans):
    sector = input()
    if sector == 'A':
        fans_a += 1
    elif sector == 'B':
        fans_b += 1
    elif sector == 'V':
        fans_v += 1
    elif sector == 'G':
        fans_g += 1

percent_a = fans_a / all_fans * 100
percent_b = fans_b / all_fans * 100
percent_v = fans_v / all_fans * 100
percent_g = fans_g / all_fans * 100
all_fans_percent = all_fans / stadium_capacity * 100

print(f'{percent_a:.2f}%')
print(f'{percent_b:.2f}%')
print(f'{percent_v:.2f}%')
print(f'{percent_g:.2f}%')
print(f'{all_fans_percent:.2f}%')