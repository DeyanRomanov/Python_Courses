divisor = int(input())
bound = int(input())

for x in range(bound, divisor - 1, -1):
    if x % divisor == 0:
        print(x)
        break
