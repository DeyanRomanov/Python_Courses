n = int(input())
for x in range(1, n + 1):
    if x == 1 or x == n:
        print(f"{(2 * n) * '*'}{n * ' '}{(2 * n) * '*'}")
    else:
        if n % 2 == 0:
            if x == n / 2:
                print(f"*{(2 * (n - 1)) * '/'}*{n * '|'}*{(2 * (n - 1)) * '/'}*")
            else:
                print(f"*{(2 * (n - 1)) * '/'}*{n * ' '}*{(2 * (n - 1)) * '/'}*")
        else:
            if x == (n + 1) / 2:
                print(f"*{(2 * (n - 1)) * '/'}*{n * '|'}*{(2 * (n - 1)) * '/'}*")
            else:
                print(f"*{(2 * (n - 1)) * '/'}*{n * ' '}*{(2 * (n - 1)) * '/'}*")
