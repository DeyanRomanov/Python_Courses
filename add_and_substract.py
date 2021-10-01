def sum_two_integers(num_1, num_2):
    return num_1 + num_2


def substract(num_1, num_2):
    return num_1 - num_2


def add_and_subst(num_1, num_2, num_3):
    print(substract(sum_two_integers(num_1, num_2), num_3))


number_one = int(input())
number_two = int(input())
number_three = int(input())

add_and_subst(number_one, number_two, number_three)
