string = 'HackerRank.com presents "Pythonist 2".'
new_string = ''
for x in string:
    if x.isalpha():
        if x.islower():
            new_string += x.upper()
        else:
            new_string += x.lower()
    else:
        new_string += x

print(new_string)