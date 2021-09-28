type_of_product = input().split('|')
budget = float(input())

products = []
profit = 0

for product in type_of_product:
    products = product.split('->')
    type_product = products[0]
    price_product = float(products[-1])
    if type_product == 'Clothes' and price_product > 50:
        continue
    elif type_product == 'Shoes' and price_product > 35:
        continue
    elif type_product == 'Accessories' and price_product > 20.50:
        continue
    if budget >= price_product:
        budget -= price_product
        profit += price_product * 1.4
        print(f'{price_product * 1.4:.2f}', end=' ')

money_for_france = budget + profit
profit -= profit / 1.4

print(f'\nProfit: {profit:.2f}')

if money_for_france > 150:
    print('Hello, France!')
else:
    print('Time to go.')


# items_and_price = input().split('|')
# budget = int(input())
#
# moment_list = []
# profit = 0
# ticket = 0
#
# for item in items_and_price:
#     moment_list = item.split('->')
#     if 'Clothes' in moment_list:
#         if 50 >= float(moment_list[-1]) and budget >= float(moment_list[-1]):
#             budget -= float(moment_list[-1])
#             print(f'{float(moment_list[-1]) * 1.4:.2f}', end=' ')
#             ticket += (float(moment_list[-1]) * 1.4)
#             profit += (float(moment_list[-1]) * 1.4) - float(moment_list[-1])
#         else:
#             continue
#     elif 'Shoes' in moment_list:
#         if 35 >= float(moment_list[-1]) and budget >= float(moment_list[-1]):
#             budget -= float(moment_list[-1])
#             print(f'{float(moment_list[-1]) * 1.4:.2f}', end=' ')
#             ticket += (float(moment_list[-1]) * 1.4)
#             profit += (float(moment_list[-1]) * 1.4) - float(moment_list[-1])
#         else:
#             continue
#     else:
#         if 20.50 >= float(moment_list[-1]) and budget >= float(moment_list[-1]):
#             budget -= float(moment_list[-1])
#             print(f'{float(moment_list[-1]) * 1.4:.2f}', end=' ')
#             ticket += (float(moment_list[-1]) * 1.4)
#             profit += (float(moment_list[-1]) * 1.4) - float(moment_list[-1])
#
# print(f'\nProfit: {profit:.2f}')
# if (ticket + budget) < 150:
#     print('Time to go.')
# else:
#     print('Hello, France!')
