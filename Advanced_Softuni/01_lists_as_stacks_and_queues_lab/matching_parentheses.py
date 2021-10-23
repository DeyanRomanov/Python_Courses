# import sys
# from io import StringIO
#
# input1 = """(2 + 3) - (2 + 3)"""
# sys.stdin = StringIO(input1)

expression = input()

expression_stack = []
for index, symbol in enumerate(expression):
    if symbol == '(':
        expression_stack.append(index)
    elif symbol == ')':
        start = expression_stack.pop()
        print(expression[start:index+1])
