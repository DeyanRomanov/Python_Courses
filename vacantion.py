budget = float(input())
season = input()
where_is = ''
place = ''
if budget <= 1000:
    place = 'Camp'
    if season == 'Summer':
        budget *= 0.65
        where_is = 'Alaska'
    elif season == 'Winter':
        budget *= 0.45
        where_is = 'Morocco'
elif budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        budget *= 0.80
        where_is = 'Alaska'
    elif season == 'Winter':
        budget *= 0.60
        where_is = 'Morocco'
elif budget > 3000:
    place = 'Hotel'
    budget *= 0.9
    if season == 'Summer':
        where_is = 'Alaska'
    elif season == 'Winter':
        where_is = 'Morocco'
print(f"{where_is} - {place} - {budget:.2f}")
