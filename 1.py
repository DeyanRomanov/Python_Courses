import math

budget = float(input())
singed_students = int(input())
floor_price = float(input())
eggs_price = float(input())
apron_price = float(input())

floor_total_price = (singed_students - (singed_students // 5)) * floor_price
apron_total_price = math.ceil(singed_students * 1.2) * apron_price
eggs_total_price = singed_students * 10 * eggs_price

total_price = floor_total_price + apron_total_price + eggs_total_price
if budget >= total_price:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    print(f'{total_price - budget:.2f}$ more needed.')

