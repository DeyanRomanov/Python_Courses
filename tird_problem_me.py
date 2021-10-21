commands = input()

delivery = {}
clients = {}
while not commands == 'End':
    command, name, money = commands.split()
    money = float(money)
    if command == 'Deliver':
        if name not in delivery:
            delivery[name] = money
        else:
            delivery[name] += money
    elif command == 'Return':
        if name in delivery and delivery[name] >= money:
            delivery[name] -= money
            if delivery[name] == 0:
                del delivery[name]
    elif command == 'Sell':
        if name not in clients:
            clients[name] = money
        else:
            clients[name] += money
    commands = input()

income = 0
for client, money in sorted(clients.items(), key=lambda x: x[0]):
    print(f'{client}: {money:.2f}')
    income += money
print('-----------')
for deliver, money in sorted(delivery.items(), key=lambda x: x[0]):
    print(f'{deliver}: {money:.2f}')
print('-----------')
print(f'Total Income: {income:.2f}')