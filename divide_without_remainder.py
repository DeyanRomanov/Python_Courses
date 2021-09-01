n = int(input())
number_2 = 0
number_3 = 0
number_4 = 0
for x in range(n):
    number = int(input())
    if number % 2 == 0:
        number_2 += 1
    if number % 3 == 0:
        number_3 += 1
    if number % 4 == 0:
        number_4 += 1
number_2 = number_2 / n * 100
number_3 = number_3 / n * 100
number_4 = number_4 / n * 100
print(f'{number_2:.2f}%')
print(f'{number_3:.2f}%')
print(f'{number_4:.2f}%')
