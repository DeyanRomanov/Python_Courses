numbers = int(input())
array = [int(x) for x in input().split()]
uniqe_array = []
for s in array:
    if array.count(s) == 1:
        uniqe_array.append(s)
print(*uniqe_array)