text = list(input())

letters_dict = {}
for letter in text:
    if letter not in letters_dict:
        letters_dict[letter] = 0
    letters_dict[letter] += 1

for letter, count in sorted(letters_dict.items(), key=lambda x: x[0]):
    print(f"{letter}: {count} time/s")
