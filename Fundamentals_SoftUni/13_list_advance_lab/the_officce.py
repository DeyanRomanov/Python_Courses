happiness = input().split()
multiplayer = int(input())

employers = len(happiness)

happiness = [int(happy) * multiplayer for happy in happiness]
average_happiness = sum(happiness) / employers
happiness = [happy for happy in happiness if int(happy) > average_happiness]

if len(happiness) >= employers / 2:
    print(f"Score: {len(happiness)}/{employers}. Employees are happy!")
else:
    print(f"Score: {len(happiness)}/{employers}. Employees are not happy!")
