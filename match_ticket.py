budget = float(input())
category = input()
group = int(input())
area = 0
if 1 <= group <= 4:
    budget *= 0.25
elif 4 < group <= 9:
    budget *= 0.4
elif 9 < group <= 24:
    budget *= 0.5
elif 24 < group <= 49:
    budget *= 0.6
else:
    budget *= 0.75
if category == 'VIP':
    area = group * 499.99
    if budget >= area:
        print(f"Yes! You have {budget - area:.2f} leva left.")
    else:
        print(f"Not enough money! You need {area - budget:.2f} leva.")
elif category == 'Normal':
    area = group * 249.99
    if budget >= area:
        print(f"Yes! You have {budget - area:.2f} leva left.")
    else:
        print(f"Not enough money! You need {area - budget:.2f} leva.")