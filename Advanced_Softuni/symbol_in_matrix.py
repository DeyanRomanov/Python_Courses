rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

searched_symbol = input()
find_it = False

for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == searched_symbol:
            print(f"({r}, {c})")
            find_it = True
            break
    if find_it:
        break

if not find_it:
    print(f"{searched_symbol} does not occur in the matrix")
