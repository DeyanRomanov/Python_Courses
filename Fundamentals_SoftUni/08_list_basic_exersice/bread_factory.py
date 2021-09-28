events = input().split('|')
energy = 100
coins = 100

is_bankrupt = False

for even in events:
    event = even.split('-')
    task = event[0]
    value = int(event[1])
    if task == 'rest':
        energy += value
        if energy > 100:
            energy = 100
            value = 0
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif task == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            print("You had to rest!")
            energy += 50
    else:
        coins -= value
        if coins > 0:
            print(f"You bought {task}.")
        else:
            print(f"Closed! Cannot afford {task}.")
            is_bankrupt = True
            break
    if is_bankrupt:
        break

if not is_bankrupt:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')


# input_string = input().split('|')
#
# moment_list = ''
# energy = 100
# coin = 100
# have_money = True
#
# for x in input_string:
#     moment_list = x.split('-')
#     if 'rest' in x:
#         if energy == 100:
#             energy = 100
#             print('You gained 0 energy.')
#         else:
#             energy += int(moment_list[-1])
#             if energy > 100:
#                 print(f'You gained {energy - 100} energy.')
#                 energy = 100
#             else:
#                 print(f'You gained {int(moment_list[-1])} energy.')
#         print(f"Current energy: {energy}.")
#     elif 'order' in x:
#         if energy >= 30:
#             energy -= 30
#             coin += int(moment_list[-1])
#             print(f"You earned {int(moment_list[-1])} coins.")
#         else:
#             print(f"You had to rest!")
#             energy += 50
#     else:
#         if coin <= int(moment_list[-1]):
#             print(f"Closed! Cannot afford {moment_list[0]}.")
#             have_money = False
#             break
#         else:
#             coin -= int(moment_list[-1])
#             print(f"You bought {moment_list[0]}.")
#     if not have_money:
#         break
#     moment_list = ''
#
# if have_money:
#     print(f"Day completed!\nCoins: {coin}\nEnergy: {energy}")
