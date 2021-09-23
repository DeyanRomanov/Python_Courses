word = input()

list = []
for index, char in enumerate(word):
    if 64 < ord(char) < 91:
        list.append(index)
print(list)
