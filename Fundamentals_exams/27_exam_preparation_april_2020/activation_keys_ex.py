activation_key = input()
text = input()

while not text == 'Generate':
    text = text.split('>>>')
    command = text[0]
    if command == 'Slice':
        start_index = int(text[1])
        end_index = int(text[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    elif command == 'Flip':
        start_index = int(text[2])
        end_index = int(text[3])
        if text[1] == 'Upper':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() \
                             + activation_key[end_index:]
        else:
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() \
                             + activation_key[end_index:]
        print(activation_key)
    elif command == 'Contains':
        substring = text[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    text = input()

print(f'Your activation key is: {activation_key}')
