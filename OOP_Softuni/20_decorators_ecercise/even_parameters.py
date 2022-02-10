def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, str) or not arg % 2 == 0:
                return f"Please use only even numbers!"
        result = func(*args)

        return result

    return wrapper


# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
