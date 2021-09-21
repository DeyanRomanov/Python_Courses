chrysanthemums = int(input())
rouse = int(input())
tulip = int(input())
season = str(input())
holiday = str(input())
price_chrysanthemums = 0
price_rouse = 0
price_tulip = 0
if season == 'Spring' or season == 'Summer':
    price_chrysanthemums = chrysanthemums * 2
    price_rouse = rouse * 4.1
    price_tulip = tulip * 2.5
elif season == 'Autumn' or season == 'Winter':
    price_chrysanthemums = chrysanthemums * 3.75
    price_rouse = rouse * 4.5
    price_tulip = tulip * 4.15
total_price = price_rouse + price_tulip + price_chrysanthemums
total_flower = rouse + tulip + chrysanthemums
if holiday == 'Y':
    total_price *= 1.15
if total_flower > 20:
    total_price *= 0.8
if season == 'Spring' and tulip > 7:
    total_price *= 0.95
if season == 'Winter' and rouse >= 10:
    total_price *= 0.9
total_price += 2
print(f'{total_price:.2f}')
