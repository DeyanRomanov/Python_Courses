array = sorted([int(x) for x in input().split()])
max_arr = sum(array[1::])
min_arr = sum(array[:-1])
print(f'{min_arr} {max_arr}')