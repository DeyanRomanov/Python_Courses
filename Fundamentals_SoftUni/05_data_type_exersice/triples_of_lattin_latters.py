number_of_letter = int(input())

for letters in range(97, 97 + number_of_letter):
    for letters_one in range(97, 97 + number_of_letter):
       for letters_two in range(97, 97 + number_of_letter):
            print(f'{chr(letters)}{chr(letters_one)}{chr(letters_two)}')
