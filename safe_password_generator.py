a_number = int(input())
b_number = int(input())
max_combination = int(input())

flag = True
password_counter = 0

for A in range(35, 56):
    for B in range(64, 97):
        for x in range(1, a_number + 1):
            for y in range(1, b_number + 1):
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                password_counter += 1
                if password_counter == max_combination or x == a_number and y == b_number:
                    flag = False
                    break
                A += 1
                B += 1
                if A > 55:
                    A = 35
                if B > 96:
                    B = 64
            if flag is False:
                break
        if flag is False:
            break
    if flag is False:
        break
