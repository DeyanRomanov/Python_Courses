import math

arr = [1, 2, 1, 3]

counter = 0
new_arr = []

for index in range(len(arr)):
    for i in range(index + 1, len(arr)):
        if index != i:
            try:
                if math.log2((arr[index] & arr[i])).is_integer():
                    counter += 1
            except ValueError:
                continue
print(counter)
