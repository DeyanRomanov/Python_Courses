matrix = []
rows = int(input())
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

flatten_matrix = [x for mat in matrix for x in mat]

print(flatten_matrix)
