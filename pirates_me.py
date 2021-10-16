cities = input()


cities_dict = {}
while not cities == 'Sail':
    city, population, gold = cities.split('||')
    population = int(population)
    gold = int(gold)
    if city not in cities_dict:
        cities_dict[city] = [population, gold]
    else:
        cities_dict[city][0] += population
        cities_dict[city][1] += gold
    cities = input()

events = input()

while not events == 'End':
    events = events.split('=>')
    command = events[0]
    if command == 'Plunder':
        town, people, money = events[1], int(events[2]), int(events[3])
        if cities_dict[town][0] > 0 or cities_dict[town][1] > 0:
            print(f"{town} plundered! {money} gold stolen, {people} citizens killed.")
            cities_dict[town][0] -= people
            cities_dict[town][1] -= money
        if cities_dict[town][0] <= 0 or cities_dict[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            cities_dict.pop(town)
    elif command == 'Prosper':
        town, money = events[1], int(events[2])
        if money < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities_dict[town][1] += money
            print(f"{money} gold added to the city treasury. {town} now has {cities_dict[town][1]} gold.")
    events = input()

if len(cities_dict) > 0:
    print(f'Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:')
    for key, value in sorted(cities_dict.items(), key=lambda x: (-x[1][1], x[0])):
        print(f'{key} -> Population: {cities_dict[key][0]} citizens, Gold: {cities_dict[key][1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
