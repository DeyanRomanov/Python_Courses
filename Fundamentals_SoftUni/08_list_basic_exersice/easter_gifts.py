gifts = input().split()
command = input()

new_list = []

while not command == 'No Money':
    new_list = []
    name = ''
    if 'OutOfStock' in command:
        new_list = command.split()
        new_list.remove('OutOfStock')
        name = ''.join(new_list)
        for x, i in enumerate(gifts):
            if i == name:
                gifts[x] = None
    elif 'Required' in command:
        new_list = command.split()
        new_list.remove('Required')
        name = int(new_list[-1])
        if name < len(gifts) and name >= 0:
            gifts[name] = new_list[0]
    elif 'JustInCase' in command:
        new_list = command.split()
        gifts[-1] = new_list[-1]
    command = input()
for x in gifts:
    if not x == None:
        print(x, end=' ')

# gifts = input().split()
# command = input()
#
# while not command == 'No Money':
#     command = command.split()
#     task = command[0]
#     new_gift = command[1]
#     if len(command) == 3:
#         index = command[2]
#     if task == 'OutOfStock':
#         for gift in range(len(gifts)):
#             if gifts[gift] == new_gift:
#                 gifts[gift] = 'None'
#     elif task == 'Required':
#         for gift in range(len(gifts)):
#             if gift == int(index):
#                 gifts.pop(gift)
#                 gifts.insert(gift, new_gift)
#     elif task == 'JustInCase':
#         gifts[-1] = new_gift
#     command = input()
#
# new_gifts_list = []
# for gift in range(len(gifts)):
#     if not gifts[gift] == 'None':
#         new_gifts_list.append(gifts[gift])
#
# print(' '.join(new_gifts_list))