secret_message = input().split()

decoding_message = []

for word in secret_message:
    first_letter = []
    new_word = []
    word = list(word)
    for letter in word:
        if letter.isnumeric():
            first_letter.append(letter)
        else:
            new_word.append(letter)
    first_letter = ''.join(first_letter)
    new_word.insert(0, chr(int(first_letter)))
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    decoding_message.append(''.join(new_word))


print(' '.join(decoding_message))
