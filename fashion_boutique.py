clothes_stack = list(map(int, input().split()))
capacity_rack = int(input())
racks = 1
current_capacity = capacity_rack

while clothes_stack:
    current_clothes = clothes_stack[-1]
    if current_clothes > current_capacity:
        racks += 1
        current_capacity = capacity_rack
    else:
        current_capacity -= clothes_stack.pop()

print(racks)