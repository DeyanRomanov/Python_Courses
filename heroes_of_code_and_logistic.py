number_of_heroes = int(input())


heroes_dict = {}
for heroes in range(number_of_heroes):
    heroes_hp_mn = input()
    hero, hit_point, mana = heroes_hp_mn.split()
    hit_point = int(hit_point)
    mana = int(mana)
    if hit_point > 100:
        hit_point = 100
    if mana > 200:
        mana = 200
    heroes_dict[hero] = [hit_point, mana]

operations = input()

while not operations == 'End':
    operations = operations.split(" - ")
    command = operations[0]
    if command == 'CastSpell':
        hero, mana_need, spell = operations[1], int(operations[2]), operations[3]
        if heroes_dict[hero][1] >= mana_need:
            heroes_dict[hero][1] -= mana_need
            print(f"{hero} has successfully cast {spell} and now has {heroes_dict[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")
    elif command == 'TakeDamage':
        hero, damage, attacker = operations[1], int(operations[2]), operations[3]
        if heroes_dict[hero][0] > damage:
            heroes_dict[hero][0] -= damage
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero][0]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes_dict[hero]
    elif command == 'Recharge':
        hero, amount = operations[1], int(operations[2])
        if heroes_dict[hero][1] + amount >= 200:
            amount = 200 - heroes_dict[hero][1]
            heroes_dict[hero][1] = 200
        else:
            heroes_dict[hero][1] += amount
        print(f"{hero} recharged for {amount} MP!")
    elif command == 'Heal':
        hero, amount = operations[1], int(operations[2])
        if heroes_dict[hero][0] + amount >= 100:
            amount = 100 - heroes_dict[hero][0]
            heroes_dict[hero][0] = 100
        else:
            heroes_dict[hero][0] += amount
        print(f"{hero} healed for {amount} HP!")
    operations = input()

for heroes, health in sorted(heroes_dict.items(), key=lambda x: (-x[1][0], x[0])):
    print(heroes)
    print(f' HP: {health[0]}')
    print(f" MP: {health[1]}")

