from collections import deque

numbers = deque(input().split())
queue = deque()
operator = ['/', '+', '-', '*']
operator_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b,
    '*': lambda a, b: a * b
}

while True:
    symbol = numbers.popleft()
    if symbol not in operator:
        queue.append(int(symbol))
    else:
        result = int(queue.popleft())
        while queue:
            number = int(queue.popleft())
            result = operator_dict[symbol](result, number)
        numbers.appendleft(result)
        if len(numbers) == 1:
            break

print(' '.join(str(x) for x in numbers))
