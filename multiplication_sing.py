def multiply_checker(num_1, num_2, num_3):
    negative_counter = 0
    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        return 'zero'
    if num_1 < 0 or num_2 < 0 or num_3 < 0:
        if num_1 < 0:
            negative_counter += 1
        if num_2 < 0:
            negative_counter += 1
        if num_3 < 0:
            negative_counter += 1
        if negative_counter == 2:
            return 'positive'
        else:
            return 'negative'
    return 'positive'


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(multiply_checker(number_one, number_two, number_three))
