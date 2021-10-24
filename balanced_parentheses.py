parentheses = input()
balanced_stack = []

is_balanced = True
searched_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}

for char in parentheses:
    if char in '({[':
        balanced_stack.append(char)
    else:
        if len(balanced_stack) < 1:
            is_balanced = False
            break
        elif not searched_dict[balanced_stack.pop()] == char:
            is_balanced = False
            break

if is_balanced and not balanced_stack:
    print('YES')
else:
    print('NO')
