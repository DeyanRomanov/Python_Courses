legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}
is_reached = False

while not is_reached:
    items = input().lower().split()
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i + 1]
        if material not in legendary_items:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity
        else:
            if material == 'shards':
                legendary_items['shards'] += quantity
                if legendary_items['shards'] >= 250:
                    legendary_items['shards'] -= 250
                    print('Shadowmourne obtained!')
                    is_reached = True
                    break
            elif material == 'fragments':
                legendary_items['fragments'] += quantity
                if legendary_items['fragments'] >= 250:
                    legendary_items['fragments'] -= 250
                    print('Valanyr obtained!')
                    is_reached = True
                    break
            elif material == 'motes':
                legendary_items['motes'] += quantity
                if legendary_items['motes'] >= 250:
                    legendary_items['motes'] -= 250
                    print('Dragonwrath obtained!')
                    is_reached = True
                    break

for key, value in sorted(legendary_items.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key}: {value}')

for key, value in sorted(junk_items.items(), key=lambda x: x[0]):
    print(f'{key}: {value}')

