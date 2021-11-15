from collections import deque


def is_valid_order(pizza_count):
    if 11 > pizza_count > 0:
        return True
    return False


orders = deque([int(n) for n in input().split(', ')])
employees = deque([int(n) for n in input().split(', ')])
total_makes_pizzas = 0


while True:
    if not orders:
        print('All orders are successfully completed!')
        print(f"Total pizzas made: {total_makes_pizzas}")
        print(f"Employees: {', '.join([str(x) for x in employees])}")
        break
    if not employees:
        print(f"Not all orders are completed.")
        print(f"Orders left: {', '.join([str(x) for x in orders])}")
        break
    order = orders.popleft()
    if not is_valid_order(order):
        continue
    employee = employees.pop()
    if order <= employee:
        total_makes_pizzas += order
        continue
    else:
        total_makes_pizzas += employee
        orders.appendleft(order - employee)
