from collections import deque

def is_done(palm_firework, willow_firework, crossette_firework):
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        return True
    return False


firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

crossette = 0
willow = 0
palm = 0

while firework_effects and explosive_power:
    effects = firework_effects.popleft()
    explosive = explosive_power.pop()
    if effects <= 0 or explosive <= 0:
        if effects <= 0 and explosive > 0:
            explosive_power.append(explosive)
            continue
        elif effects > 0 and explosive <= 0:
            firework_effects.appendleft(effects)
            continue
        else:
            continue
    if (explosive + effects) % 3 == 0 and (explosive + effects) % 5 == 0:
        crossette += 1
    elif (explosive + effects) % 3 == 0:
        palm += 1
    elif (explosive + effects) % 5 == 0:
        willow += 1
    else:
        effects -= 1
        firework_effects.append(effects)
        explosive_power.append(explosive)
    if is_done(palm, willow, crossette):
        print("Congrats! You made the perfect firework show!")
        break

if not is_done(palm, willow, crossette):
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
