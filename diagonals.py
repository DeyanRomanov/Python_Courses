rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = [matrix[x][x] for x in range(rows)]
secondary_diagonal = [matrix[x][rows - (x + 1)] for x in range(rows)]

primary_diagonal_sum = sum(primary_diagonal)
sum_of_secondary = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum_of_secondary}")
