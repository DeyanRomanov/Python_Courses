def odd_or_even(commands, *args):
    if commands == 'Odd':
        result = sum(filter(lambda x: x % 2 != 0, args)) * len(args)
    else:
        result = sum(filter(lambda x: x % 2 == 0, args)) * len(args)
    return result


command = input()
numbers = [int(x) for x in input().split()]

print(odd_or_even(command, *numbers))
