number = int(input())
area = 0
for x in range(number):
    num = int(input())
    area += num
print(f'{area / number:.2f}')
