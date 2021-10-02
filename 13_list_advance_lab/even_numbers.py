# numbers = input().split(', ')
#
# numbers = [index for index, num in enumerate(numbers) if int(num) % 2 == 0]
# print(numbers)
#



# numbers_as_string = input().split(', ')
numbers_as_string = [num for num in range(len(input().split(', '))) if int(input().split(', ')[num]) % 2 == 0]
print(numbers_as_string)
