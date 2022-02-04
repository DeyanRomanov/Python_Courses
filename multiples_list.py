# factor = int(input())
# count = int(input())
#
# numbers = []
#
# for num in range(1, (factor * count) + 1):
#     if num % factor == 0:
#         numbers.append(num)
#
# print(numbers)

number = int(input())
multiples = int(input())

list_with_multiples_numbers = [number * num for num in range(1, multiples + 1)]

print(list_with_multiples_numbers)