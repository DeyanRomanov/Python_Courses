import sys

jobs = [int(n) for n in input().split(', ')]
start_index = int(input())
target_value = jobs[start_index]
cycles = 0

while True:
    min_value = min(jobs)
    min_index = jobs.index(min_value)
    cycles += min_value
    jobs[min_index] = sys.maxsize
    if start_index == min_index:
        break

print(cycles)
