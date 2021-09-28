money = input().split(', ')
beggars = int(input())

new_list_sum = []
total_money = 0
start = 0

for beggar in range(1, beggars + 1):
    for cash in range(start, len(money), beggars):
        total_money += int(money[cash])
    new_list_sum.append(total_money)
    total_money = 0
    start += 1
print(new_list_sum)

# money = input().split(', ')
# beggars = int(input())
#
# left_side = []
# right_side = []
# sumar = 0
# sum_money_per_beggar = 0
#
# new_money_list = []
#
# for beggar in range(beggars):
#     sum_money_per_beggar = money[beggar:len(money):beggars]
#     for x in sum_money_per_beggar:
#         sumar += int(x)
#     new_money_list.append(sumar)
#     sumar = 0
#
# print(new_money_list)



# money = input().split(', ')
# beggars = int(input())
#
# beggars_money = []
# money_for_begar = 0
#
# for beggar in range(0, beggars):
#     for cash in range(beggar, len(money), beggars):
#         money_for_begar += int(money[cash])
#     beggars_money.append(money_for_begar)
#     money_for_begar = 0
# print(beggars_money)