vowels = ['A', 'E', 'I', 'O', 'U']
s = input()
a = 0
b = 0
for i, c in enumerate(s):
    if c in vowels:
        b += len(s) - i
    else:
        a += len(s) - i

if a == b:
    print("Draw")
elif a > b:
    print(f'Stuart {a}')
else:
    print(f'Kevin {b}')
