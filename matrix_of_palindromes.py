rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    line = []
    for col in range(cols):
        line.append(chr(97 + row) + chr(97 + row + col) + chr(97 + row))
    matrix.append(line)

[print(' '.join(x for x in line)) for line in matrix]
