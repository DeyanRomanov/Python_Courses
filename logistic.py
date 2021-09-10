number_of_cargos = int(input())
price_bus = 0
price_truck = 0
price_train = 0
quantity = 0

for cargos in range(number_of_cargos):
    capacity = int(input())
    if capacity <= 3:
        price_bus += (capacity * 200)
    elif 4 <= capacity <= 11:
        price_truck += (capacity * 175)
    elif capacity >= 12:
        price_train += (capacity * 120)
    quantity += capacity

total_price = (price_train + price_truck + price_bus) / quantity
percent_bus = (price_bus / 200) / quantity * 100
percent_truck = (price_truck / 175) / quantity * 100
percent_train = (price_train / 120) / quantity * 100

print(f'{total_price:.2f}\n{percent_bus:.2f}%\n{percent_truck:.2f}%\n{percent_train:.2f}%')
