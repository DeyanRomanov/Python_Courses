one_coin = int(input())
two_coin = int(input())
five_cash = int(input())
total_sum = int(input())
for one in range(0, one_coin + 1):
    for two in range(0, two_coin + 1):
        for five in range(0, five_cash + 1):
            if one + two * 2 + five * 5 == total_sum:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total_sum} lv.")
