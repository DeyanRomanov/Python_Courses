matrix = [[int(num) for num in input().split(', ')] for x in range(int(input()))]
print([num for sublist in matrix for num in sublist])
