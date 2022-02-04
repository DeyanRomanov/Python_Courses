fire_quantity = input().split('#')
water_supply = int(input())

HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

effort = 0
total_fire = 0

print('Cells:')

for fire in fire_quantity:
        fire = fire.split(' = ')
        type_of_fire = fire[0]
        range_of_fire = int(fire[1])
        if type_of_fire == 'High' and range_of_fire not in HIGH:
            continue
        elif type_of_fire == 'Medium' and range_of_fire not in MEDIUM:
            continue
        elif type_of_fire == 'Low' and range_of_fire not in LOW:
            continue
        if water_supply >= range_of_fire:
            print(f' - {range_of_fire}')
            total_fire += range_of_fire
            effort += range_of_fire * 0.25
            water_supply -= range_of_fire
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

# fires = input().split('#')
# water = int(input())
#
# new_list = []
# total_fire = 0
# effort = 0
#
# print('Cells:')
#
# for x in fires:
#     new_list = x.split()
#     x = new_list[-1]
#     if int(x) > water:
#         continue
#     if 'High' in new_list:
#         if 125 >= int(new_list[-1]) > 80:
#             x = new_list[-1]
#         else:
#             continue
#     elif 'Medium' in new_list:
#         if 80 >= int(new_list[-1]) > 50:
#             x = new_list[-1]
#         else:
#             continue
#     elif 'Low' in new_list:
#         if 50 >= int(new_list[-1]) > 0:
#             x = new_list[-1]
#         else:
#             continue
#     else:
#         continue
#     water -= int(x)
#     total_fire += int(x)
#     print(f' - {x}')
#
# effort = 25 * total_fire / 100
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {total_fire}')
