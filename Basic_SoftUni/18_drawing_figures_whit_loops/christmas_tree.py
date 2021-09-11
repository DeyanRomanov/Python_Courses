n = int(input())
for x in range(n + 1):
    if x == 0:
        print(f'{n * " "} |')
    else:
        print(f'{((n - x) * " ")}{(x * "*")} | {x * "*"}')
