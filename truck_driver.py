season = input()
kilometers = float(input())
price = 0
if season == 'Spring' or season == 'Autumn':
    if kilometers <= 5000:
        price = kilometers * 0.75
    elif kilometers <= 10000:
        price = kilometers * 0.95
    elif kilometers <= 20000:
        price = kilometers * 1.45
elif season == 'Summer':
    if kilometers <= 5000:
        price = kilometers * 0.9
    elif kilometers <= 10000:
        price = kilometers * 1.1
    elif kilometers <= 20000:
        price = kilometers * 1.45
elif season == 'Winter':
    if kilometers <= 5000:
        price = kilometers * 1.05
    elif kilometers <= 10000:
        price = kilometers * 1.25
    elif kilometers <= 20000:
        price = kilometers * 1.45
price = (price * 4) * 0.9
print(f'{price:.2f}')
