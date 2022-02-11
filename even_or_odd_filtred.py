def even_odd(*args):
    if args[-1] == 'odd':
        result = list(filter(lambda x: x % 2 != 0, args[:-1]))
    else:
        result = list(filter(lambda x: x % 2 == 0, args[:-1]))
    return result

