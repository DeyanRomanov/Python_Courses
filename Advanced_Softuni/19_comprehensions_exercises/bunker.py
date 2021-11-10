categories_input = input().split(', ')

categories = {}
count_of_items = 0
sum_of_quality = 0
categories_count = len(categories_input)

for items in categories_input:
    if items not in categories:
        categories[items] = {'quantity': 0, 'quality': 0, 'products': []}

for _ in range(int(input())):
    item, product, quantity_quality = input().split(' - ')
    quantity, quality = quantity_quality.split(';')
    quantity = quantity.split('quantity:')
    quality = quality.split('quality:')
    quantity, quality = int(quantity[1]), int(quality[1])
    if item in categories_input:
        categories[item]['products'].append(product)
        categories[item]['quantity'] += quantity
        categories[item]['quality'] += quality

for key, value in categories.items():
    count_of_items += categories[key]['quantity']
    sum_of_quality += categories[key]['quality']
print(f"Count of items: {count_of_items}")
print(f"Average quality: {sum_of_quality / categories_count:.2f}")

for k, v in categories.items():
    print(f"{k} -> {', '.join(categories[k]['products'])}")
