from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operators = deque(x for x in input().split())
honey = 0
operators_dict = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

while bees and nectar:
    bee_at_work = bees.popleft()
    nectar_to_take = nectar.pop()
    if nectar_to_take >= bee_at_work:
        operator = operators.popleft()
        if operator == '/':
            if nectar_to_take > 0:
                honey += abs(operators_dict[operator](bee_at_work, nectar_to_take))
        else:
            honey += abs(operators_dict[operator](bee_at_work, nectar_to_take))
    else:
        bees.appendleft(bee_at_work)

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
