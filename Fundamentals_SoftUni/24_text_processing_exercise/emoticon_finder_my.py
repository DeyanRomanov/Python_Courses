text = input()

for i in range(len(text)):
    if text[i] == ':' and not text[i + 1].isnumeric() and not text[i + 1] == ' ':
        print(f'{text[i]}{text[i + 1]}')
