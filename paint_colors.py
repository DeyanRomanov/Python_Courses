from collections import deque

substring = deque(x for x in input().split())

main_colors = ('red', 'yellow', 'blue')
secondary_colors = ("orange", "purple", "green")
new_colors = []

while substring:
    first_past = substring.popleft()
    if substring:
        second_past = substring.pop()
    else:
        second_past = ''

    if (first_past + second_past) in main_colors or (first_past + second_past) in secondary_colors:
        new_color = first_past + second_past
        new_colors.append(new_color)
    elif (second_past + first_past) in main_colors or (second_past + first_past) in secondary_colors:
        new_color = second_past + first_past
        new_colors.append(new_color)
    else:
        first_past = first_past[:-1]
        second_past = second_past[:-1]
        slicing = len(substring) // 2
        if first_past:
            substring.insert(slicing, first_past)
        if second_past:
            substring.insert(slicing, second_past)

secondary_dict = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
for color in new_colors:
    if color in main_colors:
        continue
    if color in secondary_colors:
        searched_color, searched_color_2 = secondary_dict[color]
        if searched_color_2 in new_colors and searched_color in new_colors:
            continue
        else:
            new_colors.remove(color)

print(new_colors)
