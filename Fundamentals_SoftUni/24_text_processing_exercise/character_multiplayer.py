first, second = input().split(' ')
total_sum = 0
if len(first) >= len(second):
    for x in range(len(second)):
        total_sum += ord(first[x]) * ord(second[x])
    for x in range(1, (len(first) - len(second)) + 1):
        total_sum += ord(first[-x])

else:
    if len(second) >= len(first):
        for x in range(len(first)):
            total_sum += ord(second[x]) * ord(first[x])
        for x in range(1, (len(second) - len(first)) + 1):
            total_sum += ord(second[-x])
print(total_sum)