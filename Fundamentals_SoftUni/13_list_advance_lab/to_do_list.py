to_do_notes = input()
sorted_to_do = [0 for _ in range(11)]
while not to_do_notes == 'End':
    to_do_notes = to_do_notes.split('-')
    importance = int(to_do_notes[0])
    note = to_do_notes[1]
    sorted_to_do.pop(importance)
    sorted_to_do.insert(importance, note)
    to_do_notes = input()

sorted_to_do = [x for x in sorted_to_do if not x == 0]
print(sorted_to_do)


# to_do_list = input().split('-')
#
# new_to_do_list = [0 for _ in range(10)]
#
# while not to_do_list == ['End']:
#     task = to_do_list[1]
#     index = int(to_do_list[0]) - 1
#     new_to_do_list.pop(index)
#     new_to_do_list.insert(index, task)
#     to_do_list = input().split('-')
# new_to_do_list = [command for command in new_to_do_list if not command == 0]
#
# print(new_to_do_list)
