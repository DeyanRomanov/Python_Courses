figures = input()
area = 0
if figures == 'square':
    side_a = float(input())
    area = side_a * side_a
elif figures == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figures == 'circle':
    import math

    radius = float(input())
    area = math.pi * math.pow(radius, 2)
elif figures == 'triangle':
    side_a = float(input())
    h_a = float(input())
    area = side_a * h_a / 2
print(f'{area:.3f}')
