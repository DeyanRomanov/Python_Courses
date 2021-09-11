n = int(input())
space = 0
for x in range(1, n):
    if x < n:
        space = (n - x) - 1
        print(f'{int(space) * " "}{x * " *"}')
for y in range(n, 0, -1):
    if y == n:
        print(f'*{(y-1) *" *"}')
    elif y != 0:
        space = (n - y) - 1
        print(f'{int(space) * " "}{y * " *"}')
