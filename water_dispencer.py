from collections import deque

people_queue = deque()
water_quantity = int(input())
people = input()
while not people == 'Start':
    people_queue.append(people)
    people = input()

commands = input()

while not commands == 'End':
    if commands.startswith('refill'):
        commands = commands.split()
        refill_water = int(commands[1])
        water_quantity += refill_water
    else:
        person_name = people_queue.popleft()
        wanted_water = int(commands)
        if water_quantity >= wanted_water:
            water_quantity -= wanted_water
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    commands = input()

print(f'{water_quantity} liters left')
