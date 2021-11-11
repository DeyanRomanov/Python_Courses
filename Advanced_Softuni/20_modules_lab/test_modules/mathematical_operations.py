def mathematics_operation(num_1, oper, num_2):
    res = ''
    opers_list = ['/', '*', '-', '+', '^']
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        print('Please enter valid numbers !')
    if oper not in opers_list:
        raise ValueError(f"Operation is not valid! Please enter valid operation('/', '*', '-', '+', '^')")
    if oper == '/':
        if num_2 <= 0:
            raise IndexError(f'Cannot device 0')
        res = num_1 / num_2
    elif oper == '*':
        res = num_1 * num_2
    elif oper == '-':
        res = num_1 - num_2
    elif oper == '+':
        res = num_1 + num_2
    elif oper == '^':
        res = num_1 ** num_2

    return f'{res:.2f}'


def fibonacci_sequence_func(number):
    fibo_nums = [0, 1]
    for x in range(2, number):
        num = fibo_nums[-1] + fibo_nums[-2]
        fibo_nums.append(num)
    return fibo_nums


def locate_func(fibo_nums, number):
    if number in fibo_nums:
        return f'The number - {number} is at index {fibo_nums.index(number)}'
    return f'The number {number} is not in the sequence'
