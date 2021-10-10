# : "{name} {price} {quantity}".
orders = input()

orders_dict = {}
while not orders == 'buy':
    name, price, quantity = orders.split()
    if name not in orders_dict:
        orders_dict[name] = [float(price), float(quantity)]
    else:
        orders_dict[name][0] = float(price)
        orders_dict[name][1] += float(quantity)
    orders = input()

for key in orders_dict:
    orders_dict[key] = orders_dict[key][0] * orders_dict[key][1]

for key, value in orders_dict.items():
    print(f'{key} -> {value:.2f}')
