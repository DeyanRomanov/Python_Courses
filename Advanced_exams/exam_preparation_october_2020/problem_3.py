import sys
from collections import deque


def best_list_pureness(*args):
    number_of_rotations = args[-1]
    list_of_numbers = deque(args[0])
    best_rotation = 0
    result_current_rotation = 0
    best_result = -sys.maxsize
    for rotation in range(number_of_rotations + 1):
        for number, index in enumerate(list_of_numbers):
            result_current_rotation += (number * index)
        if result_current_rotation > best_result:
            best_result = result_current_rotation
            best_rotation = rotation
        result_current_rotation = 0
        list_of_numbers.appendleft(list_of_numbers.pop())

    return f"Best pureness {best_result} after {best_rotation} rotations"

#
# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
