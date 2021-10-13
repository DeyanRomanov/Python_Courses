text_string = input()
text_list = [letter for letter in text_string]

explosion_size = 0

for i in range(len(text_list)):
    if text_list[i] == '>':
        explosion_size += int(text_list[i + 1])
        continue
    elif explosion_size > 0:
        explosion_size -= 1
        text_list[i] = ''

print(''.join(text_list))
