text_to_encrypt = input()
encrypted_text = ''

for letter in text_to_encrypt:
    letter = ord(letter) + 3
    encrypted_text += chr(letter)

print(encrypted_text)