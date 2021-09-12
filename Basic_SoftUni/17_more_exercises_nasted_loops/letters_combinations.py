start_interval = input()
finish_interval = input()
include_letter = input()

combination_counter = 0

for letter_a in range(ord(start_interval), ord(finish_interval) + 1):
    for letter_b in range(ord(start_interval), ord(finish_interval) + 1):
        for letter_c in range(ord(start_interval), ord(finish_interval) + 1):
            if letter_c != ord(include_letter) and letter_b != ord(include_letter) and letter_a != ord(include_letter):
                combination_counter += 1
                print(f'{chr(letter_a)}{chr(letter_b)}{chr(letter_c)}', end=' ')
print(combination_counter)
