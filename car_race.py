racers_times = input().split()

left_racer_times = racers_times[0: int((len(racers_times) - 1) / 2)]
right_racer_times = racers_times[int((len(racers_times) - 1) / 2) + 1::]

left_time = 0
right_time = 0

for times in left_racer_times:
    if int(times) == 0:
        left_time *= 0.8
    else:
        left_time += int(times)

for times in range(len(right_racer_times) - 1, -1, -1):
    times = right_racer_times[int(times)]
    if int(times) == 0:
        right_time *= 0.8
    else:
        right_time += int(times)

if right_time > left_time:
    print(f'The winner is left with total time: {left_time:.1f}')
else:
    print(f'The winner is right with total time: {right_time:.1f}')
