dwarf = input()

dwarf_dict = {}
while not dwarf == 'Once upon a time':
    name, hat, physics = dwarf.split(' <:> ')
    physics = int(physics)
    if hat not in dwarf_dict:
        dwarf_dict[hat] = {name: physics}
    else:
        if name not in dwarf_dict[hat]:
            dwarf_dict[hat].update({name: physics})
        else:
            if dwarf_dict[hat][name] < physics:
                dwarf_dict[hat][name] = physics
    dwarf = input()

print(dwarf_dict)
for key, value in sorted(dwarf_dict.items(), reverse=True, key=lambda x: len(x[1])):
    for names, physic in sorted(dwarf_dict[key].items(), reverse=True, key=lambda x: x[1]):
        print(dwarf_dict[key])
#         print(f'({key}) {dwarf_dict[key]} <-> {dwarf_dict[key][names]}')
#
# print(dwarf_dict)
