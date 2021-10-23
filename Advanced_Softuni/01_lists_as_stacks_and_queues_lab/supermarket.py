from collections import deque

names = input()

market_queue = deque()
while not names == 'End':
    if names == 'Paid':
        while market_queue:
            print(market_queue.popleft())
    else:
        market_queue.append(names)
    names = input()
print(f"{len(market_queue)} people remaining.")
