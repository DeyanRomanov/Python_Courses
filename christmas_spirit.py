quantity = int(input())
days = int(input())

budget = 0
spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += quantity * 2
        spirit += 5
    if day % 3 == 0:
        budget += (quantity * 3 + quantity * 5)
        spirit += 13
    if day % 5 == 0:
        budget += quantity * 15
        spirit += 17
    if day % 3 == 0 and day % 5 == 0:
        spirit += 30
    if day % 10 == 0:
        budget += 5 + 15 + 3
        spirit -= 20
if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
