def odd_even_calculator(number_as_string):
    even = 0
    odd = 0
    number_as_string = [int(x) for x in number_as_string]
    for x in number_as_string:
        if x % 2 == 0:
            even += x
        else:
            odd += x
    return f'Odd sum = {odd}, Even sum = {even}'


single_string = input()

print(odd_even_calculator(single_string))
