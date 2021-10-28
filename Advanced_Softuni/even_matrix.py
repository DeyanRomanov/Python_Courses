row_of_matrix = int(input())
matrix = []

for _ in range(row_of_matrix):
    matrix.append([int(x) for x in input().split(', ')])

even = []
even_matrix = []
for mat in matrix:
    even = [x for x in mat if x % 2 == 0]
    even_matrix.append(even)

print(even_matrix)