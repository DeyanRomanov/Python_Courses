needed_money = int(input())
product_price = input()
saved_money_cash = 0
saved_money_card = 0
total_saved_money = 0
counter = 1
people_cash = 0
people_card = 0
while product_price != 'End':
    product_price = int(product_price)
    counter += 1
    if counter % 2 == 0:
        if product_price <= 100:
            saved_money_cash += product_price
            people_cash += 1
            print(f"Product sold!")
        else:
            print(f"Error in transaction!")
    elif counter % 2 != 0:
        if product_price > 10:
            people_card += 1
            saved_money_card += product_price
            print(f"Product sold!")
        else:
            print(f"Error in transaction!")
    total_saved_money = saved_money_cash + saved_money_card
    if total_saved_money >= needed_money:
        print(f'Average CS: {saved_money_cash / people_cash:.2f}\nAverage CC: {saved_money_card / people_card:.2f}')
        break
    product_price = input()
if product_price == 'End':
    print(f"Failed to collect required money for charity.")
