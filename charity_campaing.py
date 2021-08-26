campaign_days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
cake_total = cakes * 45
waffles_total = waffles * 5.8
pancakes_total = pancakes * 3.2
income = ((cake_total + waffles_total + pancakes_total) * bakers) * campaign_days
cost = ((cake_total + waffles_total + pancakes_total) * bakers) * campaign_days / 8
total_profit = income - cost
print(f"{total_profit}")
