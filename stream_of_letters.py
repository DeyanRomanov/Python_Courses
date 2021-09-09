letter = input()
counter_n = 0
counter_c = 0
counter_o = 0
word = str()
while letter != 'End':
    letter = ord(letter)
    if 64 < letter < 91 or 96 < letter < 123:
        if letter == 110:
            if counter_n <= 0:
                counter_n += 1
            else:
                word += chr(letter)
        elif letter == 99:
            if counter_c <= 0:
                counter_c += 1
            else:
                word += chr(letter)
        elif letter == 111:
            if counter_o <= 0:
                counter_o += 1
            else:
                word += chr(letter)
        if counter_o == 1 and counter_c == 1 and counter_n == 1:
            print(f'{word}', end=' ')
            counter_n = 0
            counter_c = 0
            counter_o = 0
            word = str()
        if letter != 110 and letter != 111 and letter != 99:
            word += chr(letter)
    letter = input()
