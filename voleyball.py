import math
year = input()
holidays = int(input())
weekends_in_town = int(input())
holidays = holidays * 2 / 3
town = (48 - weekends_in_town) * 3 / 4
total = holidays + weekends_in_town + town
if year == 'leap':
    total *= 1.15
print(f'{math.floor(total)}')
