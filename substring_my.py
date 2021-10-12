string = input()
string_to_cut = input()

while string in string_to_cut:
    string_to_cut = string_to_cut.replace(string, '')

print(string_to_cut)
