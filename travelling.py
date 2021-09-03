destination = input()
while destination != 'End':
    needed_budget = float(input())
    while needed_budget > 0:
        money = float(input())
        needed_budget -= money
    else:
        print(f"Going to {destination}!")
    destination = input()
