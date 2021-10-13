string_to_repeat = input().split()
repeated_string = []
for i in range(len(string_to_repeat)):
    repeated_string.append(string_to_repeat[i] * len(string_to_repeat[i]))
print(''.join(repeated_string))
