numbers = int(input())
array = [int(n) for n in input().split()]
plus = []
minus = []
null = []
for x in array:
    if x < 0:
        minus.append(x)
    elif x > 0:
        plus.append(x)
    else:
        null.append(x)
print(f'{(len(plus)/numbers):.6f}')
print(f'{(len(minus)/numbers):.6f}')
print(f'{(len(null)/numbers):.6f}')
