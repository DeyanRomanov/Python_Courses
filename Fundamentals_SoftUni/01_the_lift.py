people = int(input())
wagons = [int(nums) for nums in input().split(' ')]

for x in range(len(wagons)):
    if people <= 0:
        break
    else:
        if wagons[x] == 4:
            continue
        elif wagons[x] < 4:
            if people > 4 - wagons[x]:
                a = (4 - wagons[x])
                wagons[x] += a
                people -= a
            else:
                wagons[x] += people
                people -= people

if people == 0 and min(wagons) < 4:
    wagons = [str(num) for num in wagons]
    print(f'The lift has empty spots!\n{" ".join(wagons)}')
elif people == 0 and min(wagons) == 4:
    wagons = [str(num) for num in wagons]
    print(f"{' '.join(wagons)}")
elif people > 0 and min(wagons) == 4:
    wagons = [str(num) for num in wagons]
    print(f"There isn't enough space! {people} people in a queue!\n{' '.join(wagons)}")
