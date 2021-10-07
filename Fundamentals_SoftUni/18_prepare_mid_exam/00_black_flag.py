days = int(input())
daily_plunder = int(input())
expect_plunder = int(input())
total_plunder = 0

for day in range(1, days + 1):
    if_days_is_third = daily_plunder * 1.5
    if day % 3 == 0:
        total_plunder += if_days_is_third
    else:
        total_plunder += daily_plunder
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expect_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percent_plunger = total_plunder / expect_plunder * 100
    print(f"Collected only {percent_plunger:.2f}% of the plunder.")
