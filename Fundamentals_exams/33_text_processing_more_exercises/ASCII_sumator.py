start_symbol = input()
end_symbol = input()
string = input()
sum_characters = 0

for letter in string:
    if ord(start_symbol) < ord(letter) < ord(end_symbol):
        sum_characters += ord(letter)

print(sum_characters)
