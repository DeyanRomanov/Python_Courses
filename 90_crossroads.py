from collections import deque

green_light = int(input())
window = int(input())

green_light_seconds = green_light
green_window = window
cars_queue = deque()
passed_cars_counter = 0
crash_index = ''
is_crashed = False
commands = input()

while not commands == 'END':
    if not commands == 'green':
        cars_queue.append(commands)
        pass_car = cars_queue.popleft()
        length_of_car = len(pass_car)
        if green_light_seconds < 1:
            pass
        elif green_light_seconds >= length_of_car:
            green_light_seconds -= length_of_car
            passed_cars_counter += 1
        else:
            if green_window >= (length_of_car - green_light_seconds):
                green_window -= (length_of_car - green_light_seconds)
                green_light_seconds = 0
                passed_cars_counter += 1
            else:
                is_crashed = True
                crash_index = (green_light_seconds + green_window)
                print(f"A crash happened!")
                print(f"{pass_car} was hit at {pass_car[crash_index]}.")
                break
    else:
        green_light_seconds = green_light
        green_window = window
    commands = input()

if not is_crashed:
    print("Everyone is safe.")
    print(f"{passed_cars_counter} total cars passed the crossroads.")
