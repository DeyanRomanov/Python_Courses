from collections import deque

quantity_of_food = int(input())
orders = [int(el) for el in input().split()]
print(max(orders))
# o	If you succeeded in servicing all your clients, print: "Orders complete".
# o	Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
orders = deque(orders)
while True:
    order = orders[0]
    if quantity_of_food >= order:
        quantity_of_food -= order
        orders.popleft()
        if len(orders) == 0:
            print("Orders complete")
            break
    else:
        print(f'Orders left: {" ".join(map(str, orders))}')
        break
