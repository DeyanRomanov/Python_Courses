from collections import deque

kids_names = deque(input().split())
step = int(input())

length_of_queue = len(kids_names)

while len(kids_names) > 1:
    for i in range(step):
        kids_names.append(kids_names.popleft())
    print(f'Removed {kids_names.pop()}')

print(f"Last is {kids_names.pop()}")
