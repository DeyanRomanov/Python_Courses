# "Variable times must be an integer"

try:
    text_to_repeat = input()
    time_to_repeat = int(input())
    print(text_to_repeat * time_to_repeat)
except ValueError:
    print("Variable times must be an integer")
