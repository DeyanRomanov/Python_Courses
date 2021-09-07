import math

magnolia = int(input())
hyacinth = int(input())
rouses = int(input())
cactus = int(input())
gift_price = float(input())
magnolia_price = 3.25
hyacinth_price = 4
rouses_price = 3.50
cactus_price = 8
funds = (magnolia * magnolia_price + hyacinth * hyacinth_price + rouses_price * rouses + cactus_price * cactus) * 0.95
if funds >= gift_price:
    area = funds - gift_price
    print(f'She is left with {math.floor(area)} leva.')
else:
    area = gift_price - funds
    print(f'She will have to borrow {math.ceil(area)} leva.')
