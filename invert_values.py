# single_string = input()
# new_list = single_string.split(' ')
# print_list = []
# for i in new_list:
#     i = int(i)
#     if i > 0:
#         i = -i
#     else:
#         i = abs(i)
#     print_list.append(i)
# print(print_list)

values = input().split()
opposite_values = [int(x) * -1 for x in values]
print(opposite_values)