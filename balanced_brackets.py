number_of_lines = int(input())

counter_one = 0

for line in range(number_of_lines):
    text = input()
    if text == '(':
        counter_one += 1
    elif text == ')':
        counter_one -= 1
    if counter_one < 0:
        break
    elif counter_one > 1:
        break
if not counter_one == 0:
    print('UNBALANCED')
else:
    print('BALANCED')
