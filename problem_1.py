from collections import deque

males = [int(male) for male in input().split()]
females = deque([int(females) for females in input().split()])
matches = 0

while males and females:
    male = males.pop()
    female = females.popleft()
    if male <= 0:
        females.appendleft(female)
        continue
    if female <= 0:
        males.append(male)
        continue
    if male % 25 == 0:
        if males:
            males.pop()
        females.appendleft(female)
        continue
    if female % 25 == 0:
        if females:
            females.popleft()
        males.append(male)
        continue
    if male == female:
        matches += 1
    else:
        males.append(male - 2)


print(f"Matches: {matches}")
if not males:
    print(f"Males left: none")
else:
    print(f"Males left: {', '.join(str(m) for m in males[::-1])}")
if not females:
    print(f"Females left: none")
else:
    print(f"Females left: {', '.join(str(m) for m in females)}")
