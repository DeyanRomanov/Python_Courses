targets = [int(shot) for shot in input().split()]
shot_index = input()
shot_count = 0

while not shot_index == 'End':
    shot_index = int(shot_index)
    if shot_index not in range(len(targets)):
        shot_index = input()
        continue
    else:
        current_shot = targets[shot_index]
        for index in range(len(targets)):
            target = targets[index]
            if not target == -1:
                if target > current_shot:
                    targets[index] -= current_shot
                else:
                    targets[index] += current_shot
            targets[shot_index] = -1
    shot_index = input()

shot_count = targets.count(-1)
targets = [str(shot) for shot in targets]
print(f'Shot targets: {shot_count} -> {" ".join(targets)}')
