days = int(input())
hours = int(input())

price = 0
day_price = 0
total_price = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.5
            day_price += price
        elif hour % 2 == 0 and day % 2 != 0:
            price = 1.25
            day_price += price
        else:
            price = 1
            day_price += price
    print(f"Day: {day} - {day_price:.2f} leva")
    total_price += day_price
    day_price = 0
print(f'Total: {total_price:.2f} leva')
