rows, columns = [int(x) for x in input().split()]

matrix = []
line = []
for row in range(rows):
    line = []
    for col in range(columns):
        first_symbol, last_symbol = chr(97 + row), chr(97 + row)
        middle_symbol = chr(97 + row + col)
        line.append(first_symbol + middle_symbol + last_symbol)
    matrix.append(line)

for r in range(len(matrix)):
    print(f"{' '.join(matrix[r])}")
