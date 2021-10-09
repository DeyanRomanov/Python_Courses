products_and_quantities = input().split()
searched_products = input().split()

bakery = {}

for i in range(0, len(products_and_quantities), 2):
    keys = products_and_quantities[i]
    value = products_and_quantities[i + 1]
    bakery[keys] = value


for searched in searched_products:
    if searched in bakery:
        print(f"We have {bakery[searched]} of {searched} left")
    else:
        print(f"Sorry, we don't have {searched}")
