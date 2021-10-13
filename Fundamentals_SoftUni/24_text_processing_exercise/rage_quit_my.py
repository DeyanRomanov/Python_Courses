text = input()

number = ''
output_text = ''
text_to_print = ''
for i in range(len(text)):
    if text[i].isnumeric():
        number += text[i]
        if i + 1 < len(text) and text[i + 1].isnumeric():
            continue
        else:
            text_to_print += output_text * int(number)
            number = ''
            output_text = ''
    elif not text[i].isnumeric():
        output_text += text[i]

print(f'Unique symbols used: {len(set(text_to_print.upper()))}')
print(text_to_print.upper())
