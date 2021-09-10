months = int(input())
water = 20
internet = 15
other = 0
electricity_total = 0
other_total = 0
water_total = water * months
internet_total = internet * months

for x in range(months):
    electricity = float(input())
    electricity_total += electricity
    other = (water + internet + electricity) * 1.2
    other_total += other

total_pays = (electricity_total + other_total + internet_total + water_total) / months
print(f'Electricity: {electricity_total:.2f} lv')
print(f'Water: {water_total:.2f} lv')
print(f'Internet: {internet_total:.2f} lv')
print(f'Other: {other_total:.2f} lv')
print(f'Average: {total_pays:.2f} lv')
