money = float(input())
years = int(input())
spent_money = 0

for x in range(1800, years + 1):
    if x % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + (50 * (x - 1782))
money_left = abs(money - spent_money)
if spent_money <= money:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f'He will need {money_left:.2f} dollars to survive.')
