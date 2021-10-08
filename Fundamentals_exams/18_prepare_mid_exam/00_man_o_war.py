def pirate_attack(war_ship, indx, dmg):
    if 0 <= indx < len(war_ship):
        war_ship[indx] -= dmg
        if war_ship[indx] <= 0:
            print(f"You won! The enemy ship has sunken.")
    return war_ship


def is_skins_ship(ship):
    for i in ship:
        if i <= 0:
            return True
    return False


def warship_attack(pirates, indx_1, indx_2, dmg):
    if 0 <= indx_1 < len(pirates) and 0 <= indx_2 < len(pirates):
        for i in range(indx_1, indx_2 + 1):
            pirates[i] -= dmg
            if pirates[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                return pirates
    return pirates


def repair_action(pirates, indx, healthy):
    if 0 <= indx < len(pirates):
        pirates[indx] += healthy
        if pirates[indx] > maximum_health_capacity:
            pirates[indx] = maximum_health_capacity
    return pirates


def status_action(pirates, maximum_health):
    counter = 0
    for section in pirates:
        if section < (maximum_health * 0.2):
            counter += 1
    return print(f"{counter} sections need repair.")


pirate_ship = [int(section) for section in input().split('>')]
warship = [int(section) for section in input().split('>')]
maximum_health_capacity = int(input())
commands = input()


while not commands == 'Retire':
    commands = commands.split()
    command = commands[0]
    commands.pop(0)
    if command == 'Fire':
        index, damage = int(commands[0]), int(commands[1])
        warship = pirate_attack(warship, index, damage)
        is_skin = is_skins_ship(warship)
        if is_skins_ship(warship):
            break
    elif command == 'Defend':
        index_1, index_2, damage = int(commands[0]), int(commands[1]), int(commands[2])
        pirate_ship = warship_attack(pirate_ship, index_1, index_2, damage)
        if is_skins_ship(pirate_ship):
            break
    elif command == 'Repair':
        index, health = int(commands[0]), int(commands[1])
        pirate_ship = repair_action(pirate_ship, index, health)
    elif command == 'Status':
        status_action(pirate_ship, maximum_health_capacity)
    if is_skins_ship(warship) or is_skins_ship(pirate_ship):
        break
    commands = input()

if not is_skins_ship(warship) and not is_skins_ship(pirate_ship):
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
