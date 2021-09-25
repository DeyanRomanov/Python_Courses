lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_counter = 0
expenses = 0

for losts in range(1, lost_fights + 1):
    if losts % 2 == 0:
        expenses += helmet_price
    if losts % 3 == 0:
        expenses += sword_price
        if losts % 2 == 0:
            expenses += shield_price
            shield_counter += 1
            if shield_counter == 2:
                expenses += armor_price
                shield_counter = 0
print(f"Gladiator expenses: {expenses} aureus")
