import sys

integers_in_list = [int(num) for num in input().split()]
average = 0
max_number = -sys.maxsize
big_numbers_list = []

for x in integers_in_list:
    average += x

average /= len(integers_in_list)

integers_in_list = [num for num in integers_in_list if num > average]
a = 5
if len(integers_in_list) == 0:
    print('No')
else:
    integers_in_list.sort()
    for x in integers_in_list:
        if x >= max_number:
            max_number = x
            big_numbers_list.insert(0, x)
    if len(integers_in_list) > 5:
        big_numbers_list = big_numbers_list[0:5]
        big_numbers_list = [str(x) for x in big_numbers_list]
        print(" ".join(big_numbers_list))
    else:
        big_numbers_list = [str(x)for x in big_numbers_list]
        print(' '.join(big_numbers_list))
