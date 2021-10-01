def password_len_checker(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        is_valid = False
    return is_valid


def password_digit_checker(password):
    is_valid = True
    digit_counter = 0
    for letter in password:
        if letter.isnumeric():
            digit_counter += 1
    if digit_counter < 2:
        is_valid = False
    return is_valid


def password_symbols_checker(password):
    is_valid = True
    for letter in password:
        if not letter.isalnum():
            is_valid = False
            break
    return is_valid


def total_password_checker(len_checker, digit_checker, symbols_checker):
    is_valid = True
    if not len_checker:
        is_valid = False
        print('Password must be between 6 and 10 characters')
    if not digit_checker:
        is_valid = False
        print("Password must have at least 2 digits")
    if not symbols_checker:
        is_valid = False
        print("Password must consist only of letters and digits")
    if is_valid:
        print('Password is valid')


user_password = input()

total_password_checker(password_len_checker(user_password), password_digit_checker(user_password),
                       password_symbols_checker(user_password))


# def pass_checker(password):
#     num_counter = 0
#     is_valid = True
#     if not 6 <= len(password) <= 10:
#         is_valid = False
#         print('Password must be between 6 and 10 characters')
#     for letter in password:
#         if letter.isnumeric():
#             num_counter += 1
#     for letter in password:
#         if not password.isalnum():
#             is_valid = False
#             print('Password must consist only of letters and digits')
#             break
#     if num_counter < 2:
#         is_valid = False
#         print('Password must have at least 2 digits')
#     if is_valid:
#         print("Password is valid")
#
#
# user_password = input()
#
# pass_checker(user_password)

# UPPERCASE_RANGE = range(65, 91)
# LOWERCASE_RANGE = range(97, 123)
#
#
# def valid_password(password):
#     integers_counter = 0
#     is_valid = True
#     if not 6 <= len(password) <= 10:
#         print('Password must be between 6 and 10 characters')
#         is_valid = False
#     symbol = [x for x in password if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']]
#     if len(symbol) < 2:
#         print("Password must have at least 2 digits")
#         is_valid = False
#     for symbol in password:
#         if symbol not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and
#         ord(symbol) not in UPPERCASE_RANGE and ord(
#                 symbol) not in LOWERCASE_RANGE:
#             print("Password must consist only of letters and digits")
#             is_valid = False
#             break
#     if is_valid:
#         print("Password is valid")
#
#
# try_password = input()
#
# valid_password(try_password)

# def is_password_length_valid(password: str):
#     if 6 <= len(password) <= 10:
#         return True
#
#     return False
#
#
# def is_password_alphanumeric(password: str):
#     is_alphanum = True
#
#     for ch in password:
#         if not (ch.isalpha() or ch.isnumeric()):
#             # not alphanumeric -> some symbols
#             is_alphanum = False
#             break
#
#     return is_alphanum
#
#
# def does_password_have_at_least_two_digits(password: str):
#     digits_cnt = 0
#
#     for ch in password:
#         if ch.isnumeric():
#             digits_cnt += 1
#
#     if digits_cnt >= 2:
#         return True
#     else:
#         return False
#
#
# def validate_password(password: str):
#     is_valid = True
#
#     if not is_password_length_valid(password):
#         print('Password must be between 6 and 10 characters')
#         is_valid = False
#
#     if not is_password_alphanumeric(password):
#         print('Password must consist only of letters and digits')
#         is_valid = False
#
#     if not does_password_have_at_least_two_digits(password):
#         print('Password must have at least 2 digits')
#         is_valid = False
#
#     if is_valid:
#         print('Password is valid')
#
#
# password_input = input()
#
# validate_password(password_input)
