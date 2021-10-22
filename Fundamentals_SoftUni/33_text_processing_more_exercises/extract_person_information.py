number_of_strings = int(input())

for strings in range(number_of_strings):
    string = input()
    for index, letter in enumerate(string):
        if letter == '@':
            start_index_name = index + 1
        if letter == '|':
            end_index_name = index
        if letter == '#':
            start_age_index = index + 1
        if letter == '*':
            end_age_index = index
    name = string[start_index_name:end_index_name]
    age = string[start_age_index:end_age_index]
    print(f"{name} is {age} years old.")
