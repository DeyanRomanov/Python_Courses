def exchange_command(nums: list, indx: int):
    nums = nums[indx + 1:] + nums[:indx + 1]
    return nums


def odd_even_checker(nums, odd_even):
    if odd_even == 'odd':
        odd_even_list = [int(x) for x in nums if not int(x) % 2 == 0]
    else:
        odd_even_list = [int(x) for x in nums if int(x) % 2 == 0]
    return odd_even_list


def max_command(nums, odd_even):
    if not len(odd_even_checker(nums, odd_even)) == 0:
        max_list = odd_even_checker(nums, odd_even)
        max_number = max(max_list)
        for i in range(len(nums) - 1, -1, -1):
            if int(nums[i]) == max_number:
                return print(i)
    return print("No matches")


def min_command(nums, odd_even):
    if not len(odd_even_checker(nums, odd_even)) == 0:
        min_list = odd_even_checker(nums, odd_even)
        min_number = min(min_list)
        for i in range(len(nums) - 1, -1, -1):
            if int(nums[i]) == min_number:
                return print(i)
    return print('No matches')


def first_command(numbs, indx, odd_even):
    odd_even_list = odd_even_checker(numbs, odd_even)
    first_list = []
    if indx <= len(numbs):
        for num in odd_even_list:
            first_list.append(num)
            indx -= 1
            if indx <= 0:
                break
        return print(first_list)
    return print("Invalid count")


def last_command(numbs, indx, odd_even):
    last_list = []
    odd_even_list = odd_even_checker(numbs, odd_even)
    if odd_even_list is None:
        return print(last_list)
    if indx <= len(numbs):
        for i in range(len(odd_even_list) - 1, -1, -1):
            last_list.append(odd_even_list[i])
            indx -= 1
            if indx <= 0:
                break
        return print(last_list[::-1])
    return print("Invalid count")


numbers = input().split()
numbers = [num for num in numbers]
command = input()

while not command == 'end':
    command = command.split()
    task = command[0]
    if task == 'exchange':
        index = int(command[1])
        if 0 < index <= len(numbers):
            numbers = exchange_command(numbers, index)
        else:
            print('Invalid index')
    elif task == 'max':
        odd_even_counter = command[1]
        max_command(numbers, odd_even_counter)
    elif task == 'min':
        odd_even_counter = command[1]
        min_command(numbers, odd_even_counter)
    elif task == 'first':
        odd_even_counter = command[2]
        index = int(command[1])
        first_command(numbers, index, odd_even_counter)
    elif task == 'last':
        odd_even_counter = command[2]
        index = int(command[1])
        last_command(numbers, index, odd_even_counter)
    command = input()

numbers = [int(x) for x in numbers]
print(numbers)
