from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk_cups = deque([int(x) for x in input().split(', ')])
milkshakes = 0
do_it = False

while chocolate and milk_cups:

    choco = chocolate.pop()
    cup = milk_cups.popleft()
    if choco <= 0 and cup <= 0:
        continue
    if choco <= 0:
        milk_cups.appendleft(cup)
        continue
    if cup <= 0:
        chocolate.append(choco)
        continue
    if choco == cup:
        milkshakes += 1
        if milkshakes == 5:
            do_it = True
            break
    else:
        chocolate.append(choco - 5)
        milk_cups.append(cup)

if do_it:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if not chocolate:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join(str(num) for num in chocolate)}")
if not milk_cups:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join(str(num) for num in milk_cups)}")
