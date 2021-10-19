numbers_of_plant = int(input())
plants_dict = {}

for plants in range(numbers_of_plant):
    plant, rarities = input().split('<->')
    rarities = int(rarities)
    if plant not in plants_dict:
        plants_dict[plant] = {'rarity': rarities, 'rating': []}

commands = input()

while not commands == 'Exhibition':
    commands = commands.split(': ')
    command = commands[0]
    if command == 'Rate':
        plant, rating = commands[1].split(' - ')
        rating = int(rating)
        if plant in plants_dict:
            plants_dict[plant]['rating'].append(rating)
        else:
            print('error')
    elif command == 'Update':
        plant, new_rarity = commands[1].split(' - ')
        new_rarity = int(new_rarity)
        if plant in plants_dict:
            plants_dict[plant]['rarity'] = new_rarity
        else:
            print('error')
    elif command == 'Reset':
        plant = commands[1]
        if plant in plants_dict:
            plants_dict[plant]['rating'] = []
        else:
            print('error')

    commands = input()

print('Plants for the exhibition:')
for plant, value in plants_dict.items():
    if not value['rating']:
        plants_dict[plant]['rating'] = 0
    else:
        plants_dict[plant]['rating'] = sum(plants_dict[plant]['rating']) / len(plants_dict[plant]['rating'])
for key, value in sorted(plants_dict.items(), key=lambda x: (x[1]['rarity'], x[1]['rating']), reverse=True):
    print(f"- {key}; Rarity: {plants_dict[key]['rarity']}; Rating: {plants_dict[key]['rating']:.2f}")
