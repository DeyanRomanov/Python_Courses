import math

days = int(input())
kg_food_left = int(input())
dogs_food = float(input())
cats_food = float(input())
turtle_food = float(input())
turtle_food /= 1000
need_food = days * (dogs_food + cats_food + turtle_food)
if kg_food_left >= need_food:
    area = kg_food_left - need_food
    print(f'{math.floor(area)} kilos of food left.')
else:
    area = need_food - kg_food_left
    print(f'{math.ceil(area)} more kilos of food are needed.')
