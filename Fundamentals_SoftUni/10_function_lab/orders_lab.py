def bill(ords, value):
    bills = 0
    if ords == 'coffee':
        bills = value * 1.50
    elif ords == 'coke':
        bills = value * 1.40
    elif ords == 'water':
        bills = value * 1
    elif ords == 'snacks':
        bills = value * 2
    return bills


orders = input()
quantity = int(input())

print(f'{bill(orders, quantity):.2f}')
