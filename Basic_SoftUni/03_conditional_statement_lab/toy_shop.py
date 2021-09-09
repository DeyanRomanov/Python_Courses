excursion = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
puzzles_price = 2.60
dolls_price = 3.00
teddy_bears_price = 4.10
minions_price = 8.20
trucks_price = 2.00
total_games = puzzles + dolls + teddy_bears + minions + trucks
total = puzzles * puzzles_price + dolls * dolls_price + teddy_bears_price * teddy_bears + \
        minions_price * minions + trucks_price * trucks
if total_games >= 50:
    total *= 0.75
rent = total * 0.1
total -= rent
area = 0
if excursion <= total:
    area = total - excursion
    print(f'Yes! {area:.2f} lv left.')
else:
    area = excursion - total
    print(f'Not enough money! {area:.2f} lv needed.')
