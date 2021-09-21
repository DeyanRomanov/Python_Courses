type_fuel = str(input()).lower()
litters = float(input())
club_card = str(input()).lower()

price = 0

if club_card == 'no':
    if type_fuel == 'gas':
        price = litters * 0.93
    elif type_fuel == 'gasoline':
        price = litters * 2.22
    elif type_fuel == 'diesel':
        price = litters * 2.33
elif club_card == 'yes':
    if type_fuel == 'gas':
        price = litters * 0.85
    elif type_fuel == 'gasoline':
        price = litters * 2.04
    elif type_fuel == 'diesel':
        price = litters * 2.21
if 20 <= litters <= 25:
    price *= 0.92
elif litters > 20:
    price *= 0.9
print(f'{price:.2f} lv.')
