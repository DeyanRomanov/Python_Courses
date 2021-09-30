def calculate(oper, num_1, num_2):
    result = ''
    if oper == 'multiply':
        result = num_1 * num_2
    elif oper == 'divide':
        result = num_1 // num_2
    elif oper == 'add':
        result = num_1 + num_2
    elif oper == 'subtract':
        result = num_1 - num_2
    return result


operator = input()
number_one = int(input())
number_two = int(input())

print(calculate(operator, number_one, number_two))
