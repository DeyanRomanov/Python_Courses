def math_operations(*args, **kwargs):
    args = list(args)
    while args:
        number = args.pop(0)
        kwargs['a'] += number
        if args:
            number = args.pop(0)
            kwargs['s'] -= number
        if args:
            number = args.pop(0)
            if not number == 0:
                kwargs['d'] /= number
        if args:
            number = args.pop(0)
            kwargs['m'] *= number
    return kwargs


# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
