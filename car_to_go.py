budget = float(input())
season = input()
clas = ''
types = ''
price = 0
if budget <= 100:
    clas = 'Economy class'
    if season == 'Summer':
        price = budget * 0.35
        types = 'Cabrio'
    elif season == 'Winter':
        price = budget * 0.65
        types = 'Jeep'
elif budget <= 500:
    clas = 'Compact class'
    if season == 'Summer':
        price = budget * 0.45
        types = 'Cabrio'
    elif season == 'Winter':
        price = budget * 0.80
        types = 'Jeep'
elif budget > 500:
    clas = 'Luxury class'
    types = 'Jeep'
    price = budget * 0.9
print(f'{clas}\n{types} - {price:.2f}')
