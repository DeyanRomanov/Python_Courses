from collections import deque

material = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
present_dict = {
    150: {'name': 'Doll', 'numbers': 0},
    250: {'name': 'Wooden train', 'numbers': 0},
    300: {'name': 'Teddy bear', 'numbers': 0},
    400: {'name': 'Bicycle', 'numbers': 0}
                }

doll_and_train = 0
teddy_and_bicycle = 0
its_done = False

while material and magic_level:
    current_material = material.pop()
    current_magic = magic_level.popleft()
    result = current_magic * current_material
    if current_material == 0 or current_magic == 0:
        if current_material == 0 and current_magic == 0:
            continue
        elif current_magic == 0:
            material.append(current_material)
            continue
        elif current_material == 0:
            magic_level.appendleft(current_magic)
            continue
    elif result in present_dict:
        toy = present_dict[result]['name']
        for key, values in present_dict.items():
            if toy == values['name']:
                present_dict[result]['numbers'] += 1
    elif result < 0:
        result = current_magic + current_material
        material.append(result)
    elif result > 0 and result not in present_dict:
        material.append(current_material + 15)

if present_dict[150]['numbers'] > 0 and present_dict[250]['numbers'] > 0:
    its_done = True
elif present_dict[300]['numbers'] > 0 and present_dict[400]['numbers'] > 0:
    its_done = True
if its_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if material:
    print(f"Materials left: {', '.join(str(x) for x in reversed(material))}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in sorted(present_dict.items(), key=lambda x: x[1]['name']):
    if value['numbers'] > 0:
        print(f"{value['name']}: {value['numbers']}")
