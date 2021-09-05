n = int(input())
lenght = int(input())
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(97, 97 + lenght):
            for d in range(97, 97 + lenght):
                for h in range(1, n + 1):
                    if h > x and h > y:
                        print(f'{x}{y}{chr(z)}{chr(d)}{h}', end=' ')
