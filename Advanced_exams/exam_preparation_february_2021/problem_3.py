def stock_availability(boxes: list, command, *args):
    args = list(args)
    if command == 'delivery':
        boxes.extend(args)
        return boxes
    elif command == 'sell':
        if len(args) == 0:
            boxes.pop(0)
            return boxes
        elif isinstance(args[0], int):
            for _ in range(args[0]):
                if boxes:
                    boxes.pop(0)
                else:
                    break
            return boxes
        else:
            for stock in args:
                if stock in boxes:
                    while stock in boxes:
                        boxes.remove(stock)
            return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
