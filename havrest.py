import math


x = int(input())
y = float(input())
z = int(input())
workers = int(input())
kg = x * y
for_wine = kg * 0.4 / 2.5
for_workers = 0
if z <= for_wine:
    print(f'Good harvest this year! Total wine: {math.floor(for_wine)} liters.')
    for_workers = (for_wine - z) / workers
    area = for_wine - z
    print(f'{math.ceil(area)} liters left -> {math.ceil(for_workers)} liters per person.')
else:
    area = z - for_wine
    print(f'It will be a tough winter! More {math.floor(area)} liters wine needed.')
