usernames = input().split(', ')
for user in usernames:
    is_valid = False
    if 2 < len(user) < 17:
        for letter in user:
            if letter == '_' or letter == '-' or letter.isalnum():
                is_valid = True
            else:
                is_valid = False
                break
    if is_valid:
        print(user)

# •	has length between 3 and 16 characters inclusive
# •	contains only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after or in between