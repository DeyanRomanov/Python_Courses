food_and_quantity = input().split()

my_bakery = {}

for i in range(0, len(food_and_quantity), 2):
    keys = food_and_quantity[i]
    values = food_and_quantity[i + 1]
    my_bakery[keys] = int(values)

print(my_bakery)