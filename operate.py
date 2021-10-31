from functools import reduce


# def operate(operator, *args):
#     result = 0
#     if operator == '+':
#         for n in args:
#             result += n
#         return result
#     elif operator == '-':
#         result = args.index(0)
#         for n in range(1, len(args)):
#             result -= n
#     elif operator == '/':
#         result = args.index(0)
#         for n in range(1, len(args)):
#             n = args[n]
#             result /= n
#     elif operator == '*':
#         result = 1
#         for n in args:
#             result *= n
#     return result


def operate(operator, *args):
    if operator == '+':
        return reduce(lambda x, y: x + y, args)
    elif operator == '-':
        return reduce(lambda x, y: x - y, args)
    elif operator == '*':
        return reduce(lambda x, y: x * y, args)
    elif operator == '/':
        return reduce(lambda x, y: x / y, args)


arguments = input().split(', ')
oper = arguments[0]
argument = [int(x) for x in arguments[1:]]
print(operate(oper, *argument))
