text = input().split()

text_dict = {}

for word in text:
    for letter in word:
        if letter not in text_dict:
            text_dict[letter] = 0
        text_dict[letter] += 1

for key, value in text_dict.items():
    print(f'{key} -> {value}')
