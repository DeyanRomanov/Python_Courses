key = int(input())
lines = int(input())

secret_message = ''

for line in range(lines):
    letter = input()
    secret_message += chr(ord(letter) + key)

print(secret_message)
