def char_permutation(text, counter):
    if len(text) == counter:
        return print(text)
    for x in range(len(text)):
        counter += 1
        text.append(text.pop(x + 1))
        char_permutation(text, counter)


text_input = list(input())
counter = 0
char_permutation(text_input, counter)
