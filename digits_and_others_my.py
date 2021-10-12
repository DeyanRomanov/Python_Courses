digits_and_others = input()
digits = ''
letters = ''
others = ''

for sing in digits_and_others:
    if sing.isnumeric():
        digits += sing
    elif sing.isalpha():
        letters += sing
    else:
        others += sing

print(f'{digits}\n{letters}\n{others}')