def jumping(neighborhoods, jump):
    if neighborhoods[jump] == 0:
        print(f"Place {jump} already had Valentine's day.")
    elif neighborhoods[jump] >= 2:
        neighborhoods[jump] -= 2
        if neighborhoods[jump] == 0:
            print(f"Place {jump} has Valentine's day.")
    return neighborhoods


our_neighborhoods = [int(num) for num in input().split('@')]
jump_commands = input()
jumper = 0

while not jump_commands == 'Love!':
    jump_commands = jump_commands.split()
    command = jump_commands[0]
    index = int(jump_commands[1])
    jumper += index
    if jumper >= len(our_neighborhoods):
        jumper = 0
    if command == 'Jump':
        our_neighborhoods = jumping(our_neighborhoods, jumper)
    jump_commands = input()

print(f"Cupid's last position was {jumper}.")
if max(our_neighborhoods) == 0:
    print(f"Mission was successful.")
else:
    while 0 in our_neighborhoods:
        our_neighborhoods.remove(0)
    print(f"Cupid has failed {len(our_neighborhoods)} places.")
