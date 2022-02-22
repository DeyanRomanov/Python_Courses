usernames = []
for user in range(int(input())):
    usernames.append(input())


def swap_string(user):
    possible = []
    for x in user:
        possible.append(ord(x))
    possible.sort()
    a = ''
    for x in possible:
        a += chr(x)

    return a


def get_is_valid(username):
    result = []
    for users in username:
        a = users
        if swap_string(users) < a:
            result.append('YES')
        else:
            result.append('NO')
    return result


for user in usernames:
    print(get_is_valid(usernames))
