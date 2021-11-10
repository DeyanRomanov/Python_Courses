matrix = [[int(num) for num in input().split(', ')] for _ in range(int(input()))]

first_diagonal = [matrix[num][num] for num in range(len(matrix))]
second_diagonal = [matrix[num][len(matrix[0]) - 1 - num] for num in range(len(matrix[0]))]

print(f"First diagonal: {', '.join(str(num) for num in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(str(num) for num in second_diagonal)}. Sum: {sum(second_diagonal)}")
