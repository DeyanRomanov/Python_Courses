entered_money = input()
card_money = 0
while entered_money != 'NoMoreMoney':
    entered_money = float(entered_money)
    if entered_money <= 0:
        print(f"Invalid operation!")
        break
    card_money += entered_money
    print(f'Increase: {entered_money:.2f}')
    entered_money = input()
print(f"Total: {card_money:.2f}")
