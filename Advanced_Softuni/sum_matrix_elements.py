row, columns = [int(x) for x in input().split(', ')]

matrix = []

for x in range(row):
    ll = [int(x) for x in input().split(', ')]
    matrix.append(ll)

sum_matrix = 0

for mat in matrix:
    sum_matrix += sum(mat)

print(sum_matrix)
print(matrix)
