def multiply(times):

    def decorator(func):

        def wrapper(number):
            result = times * func(number)

            return result

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
