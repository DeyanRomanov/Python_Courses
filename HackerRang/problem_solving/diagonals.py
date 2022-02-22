size = int(input())
matrix = []
for row in range(size):
    matrix.append([int(x) for x in input().split()])

left_diagonal = []
right_diagonal = []

for rol in range(len(matrix)):
    left_diagonal.append(matrix[len(matrix)-1-rol][len(matrix)-1-rol])
    right_diagonal.append(matrix[len(matrix)-1-rol][rol])

print(abs(sum(right_diagonal) - sum(left_diagonal)))
