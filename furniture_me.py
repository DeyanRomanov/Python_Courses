import re


furniture = input()
total_price = 0

print(f'Bought furniture:')
while not furniture == 'Purchase':
    pattern = r"\>{2}(?P<Product>[A-Za-z0-9]+)\<{2}(?P<Price>\d+\.?[0-9]*)\!(?P<Quantity>[0-9]+)"

    result = re.finditer(pattern, furniture)
    for res in result:
        total_price += (float(res.group('Price')) * int(res.group('Quantity')))
        print(res.group('Product'))
    furniture = input()

print(f'Total money spend: {total_price:.2f}')
