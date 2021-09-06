x = float(input())
y = float(input())
h = float(input())
window = 1.5 * 1.5
door = 2 * 1.20
triangle = 2 * (h * x / 2)
ceiling = 2 * x * y
wall_1 = x * x + x * x - door
wall_2 = 2 * x * y - 2 * window
green = (wall_1 + wall_2) / 3.4
red = (triangle + ceiling) / 4.3
print(f'{green:.2f}')
print(f'{red:.2f}')
