class ValueTooSmall(Exception):
    pass


class NegativeValue(Exception):
    pass


class ValueTooBig(Exception):
    pass


numbers = 0

for _ in range(5):
    numbers = int(input())
    if numbers < 0:
        raise NegativeValue
    elif numbers > 100:
        raise ValueTooBig
    elif numbers < 10:
        raise ValueTooSmall
    else:
        print('Good Numbers')

