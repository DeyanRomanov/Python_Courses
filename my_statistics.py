product_in_stock = input()

products_dict = {}

while not product_in_stock == 'statistics':
    product, quantity = product_in_stock.split(': ')
    quantity = int(quantity)
    if product not in products_dict:
        products_dict[product] = 0
    products_dict[product] += quantity
    product_in_stock = input()

print('Products in stock:')

for key, value in products_dict.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(products_dict)}')
print(f'Total Quantity: {sum(products_dict.values())}')
