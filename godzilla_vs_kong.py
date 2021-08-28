budget = float(input())
statists = int(input())
price_clothes = float(input())
decor = budget * 0.1
if statists >= 150:
    price_clothes *= 0.9
funds_statists = statists * price_clothes
total_funds = funds_statists + decor
if budget >= total_funds:
    area = budget - total_funds
    print(f"Action!\nWingard starts filming with {area:.2f} leva left.")
elif budget < total_funds:
    area = total_funds - budget
    print(f'Not enough money!\nWingard needs {area:.2f} leva more.')
