n = int(input())
s = set(map(int, input().split()))
for x in range(int(input())):
    command = input().split()
    if len(command) > 1:
        command, index = command[0], int(command[1])
    else:
        command = command[0]
    if command == 'pop':
        if s:
            s.pop()
        else:
            raise KeyError
    elif command == 'remove':
        if index in s:
            s.remove(index)
        else:
            raise KeyError
    elif command == 'discard':
        if index in s:
            s.discard(index)
        else:
            continue

print(sum(s))
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5