price = input()
total_price = 0

while True:
    if price == 'special' or price == 'regular':
        break
    price = float(price)
    if price < 0:
        print('Invalid price!')
    else:
        total_price += price
    price = input()

if total_price == 0:
    print('Invalid order!')
else:
    taxes = total_price * 0.2
    total_price_whit_taxes = total_price + taxes
    if price == 'special':
        total_price_whit_taxes *= 0.9
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f'-----------')
    print(f'Total price: {total_price_whit_taxes:.2f}$')
