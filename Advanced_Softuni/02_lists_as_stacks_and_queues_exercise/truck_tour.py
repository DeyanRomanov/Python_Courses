from collections import deque


stops = int(input())
queue = deque()

for _ in range(stops):
    pumps = [int(pump) for pump in input().split()]
    queue.append(pumps)


index_to_start = 0
while True:
    is_completed = True
    fuel_tank = 0
    for fuel, kilometers in queue:
        fuel_tank += fuel
        if fuel_tank < kilometers:
            is_completed = False
            break
        fuel_tank -= kilometers
    if not is_completed:
        queue.append(queue.popleft())
        index_to_start += 1
    else:
        break

print(index_to_start)
