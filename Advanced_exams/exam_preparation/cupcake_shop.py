def deliveries(inventory, *args):
    for box in args:
        inventory.append(box)
    return inventory


def sells(inventory, *args):
    if len(args) == 0:
        inventory.pop(0)
        return inventory
    elif isinstance(args[0], int):
        for i in range(args[0]):
            if inventory:
                inventory.pop(0)
            else:
                break
        return inventory
    else:
        for box in args:
            while box in inventory:
                inventory.remove(box)
        return inventory


def stock_availability(inventory, command, *args):
    if command == 'delivery':
        inventory = deliveries(inventory, *args)
    else:
        inventory = sells(inventory, *args)
    return inventory


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
