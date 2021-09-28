numbers = [int(num) for num in input().split()]
numbers_to_remove = int(input())

for number in range(numbers_to_remove):
    numbers.remove(min(numbers))

numbers = [str(num) for num in numbers]
print(', '.join(numbers))

# import sys
#
# number_as_string = input().split()
# number_to_remove = int(input())
#
# number_as_numbers = ''
#
# min_number = sys.maxsize
#
# for x in range(number_to_remove):
#     min_number = sys.maxsize
#     for index, num in enumerate(number_as_string):
#         num = int(num)
#         if num < min_number:
#             min_number = num
#     number_as_string.remove(str(min_number))
# for y, x in enumerate(number_as_string):
#     if y < len(number_as_string) - 1:
#         print(f'{int(x)}, ', end='')
#     else:
#         print(f'{int(x)}')
