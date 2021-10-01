def is_palindrome_number(numbers_as_string):
    for nums in numbers_as_string:
        if nums == nums[::-1]:
            print(True)
        else:
            print(False)
    # for number in numbers_as_string:
        # is_palindrome = True
        # num = [int(x) for x in number]
        # left_side_of_number = num[:len(num) // 2]
        # right_side_of_number = num[(len(num) - 1) // 2:]
        # right_side_of_number = right_side_of_number[::-1]
        # for x in range(len(left_side_of_number)):
        #     if not left_side_of_number[x] == right_side_of_number[x]:
        #         is_palindrome = False
        #         break
        # if not is_palindrome:
        #     print(False)
        # else:
        #     print(True)


list_of_numbers_as_string = input().split(', ')

is_palindrome_number(list_of_numbers_as_string)
