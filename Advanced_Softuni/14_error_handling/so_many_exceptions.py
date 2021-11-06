""" This code raises many exceptions. Fix it, so it works correctly."""

# numbers_list = input().split(", ")
# result = 0
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
#
# print(result)
#               Examples
#   input                                           output
#   1, 4, 5                                         20
#   4, 5, 6, 1, 3                                   10.0
#   2, 5, 10                                         1.0
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11                 0.003968253968253968

numbers_list = [int(num) for num in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
