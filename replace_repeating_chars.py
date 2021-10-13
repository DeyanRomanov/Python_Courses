text = input()

new_text = ''

for letter in text:
    if len(new_text) < 1:
        new_text += letter
    else:
        if not new_text[-1] == letter:
            new_text += letter

print(new_text)